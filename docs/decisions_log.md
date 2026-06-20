# Assumptions & Decisions Log

## Section 2/3 — Calendar Data Price Field

**Date:** June 19, 2026
**Finding:** `calendar.csv.gz` price/adjusted_price fields are 100% null for 
Amsterdam (all 3.8M rows).

**Decision:** Cannot compute per-day revenue from calendar data as originally 
planned. Will instead use `listings.csv.gz`'s `price` field (static, current 
price) combined with `estimated_occupancy_l365d` and `estimated_revenue_l365d` 
— which Inside Airbnb already provides pre-calculated — for revenue-related 
analysis. Calendar's `available` field remains usable for occupancy-rate 
calculations.

**Trade-off accepted:** Revenue estimates rely on Inside Airbnb's own 
pre-computed methodology rather than a custom calculation, so we inherit 
whatever assumptions they used (not transparent to us).

## Section 3.1 — Price Outlier Threshold Decision (Final)

**Date:** June 20, 2026

**Options considered:**
1. Leave all prices as-is and accept that extreme values (up to 
   €80,018/night) distort means, distributions, and any regression 
   using price as a feature.
2. Drop high-price rows entirely from the dataset.
3. Cap/winsorize prices at a fixed statistical percentile (e.g., 99th), 
   regardless of whether the values are confirmed errors or just 
   legitimately expensive.
4. Manually investigate the most extreme values, confirm which are 
   genuine errors vs. real (if extreme) listings, then flag — not 
   delete — the confirmed errors. (CHOSEN)

**Why this approach:** Option 1 was rejected because the magnitude of 
distortion is severe — a single €80,018 row can shift a mean for 5,874 
listings noticeably. Option 2 was rejected because deleting rows 
destroys information permanently and removes listings that may be 
useful for non-price analysis (e.g., location, amenities). Option 3 
was rejected because a blind percentile cutoff would have excluded 
some legitimate high-capacity listings (e.g., "ShipStays" at €5,200/
night for 16 guests) while still potentially missing genuine errors 
that fall just under the cutoff. Option 4 was chosen because manual 
inspection of listing names directly confirmed specific rows as errors 
("Havenlodge" at €80,018, "test host, don't book") versus others that, 
while extreme, had no such evidence (ShipStays).

**Method:** Applied the IQR method first, which flagged 301 listings 
(5.1% of non-null prices) as high-end outliers (upper bound: €543.50/
night) — too broad to be useful on its own. Inspected the full price 
distribution above €2,000 to find a natural break point, combined with 
manual name-based verification of the most extreme listings.

**Finding:** Prices form a continuous, plausible distribution up to 
~€2,975 (round-number clustering at €500 suggests deliberate host 
pricing, not errors). A moderate, unconfirmed jump occurs at 
€3,930–€13,978 (6 listings). A clear, severe break occurs at €40,000+ 
(5 listings), independently confirmed via listing names as data entry 
errors or test listings (e.g., two "Havenlodge" listings at €80,018/
night for 4 guests, multiple "Hotel room" listings at €40,000-€50,000 
for 2-6 guests, and one listing literally named "test host, don't 
book").

**Decision:** 
- Listings priced ≥ €40,000/night (5 listings) flagged via a new 
  boolean column `price_outlier_flag = True` and excluded from all 
  price-based statistics, distributions, and modeling.
- Listings priced €3,930–€13,978 (6 listings) kept but visually 
  reviewed in EDA — flagged in commentary only, not excluded.
- Raw price column never modified; flag is additive.

**Trade-off accepted:** A hard cutoff at exactly €40,000 is somewhat 
arbitrary at the boundary, but justified by the combination of a 
visible statistical gap and independent name-based confirmation. We 
accept the small risk that 1-2 borderline rows near the cutoff could 
be misclassified in either direction.

---

## Section 3.1 — reviews.csv "Duplicate" Investigation

**Date:** June 20, 2026

**Options considered:**
1. Automatically drop all 27,545 rows flagged as exact-match duplicates 
   by the profiling script.
2. Ignore the duplicate flag entirely and proceed without checking.
3. Cross-reference flagged rows against the detailed reviews.csv.gz 
   file (which has unique review IDs) before deciding. (CHOSEN)

**Why this approach:** Option 1 was rejected because reviews.csv only 
contains listing_id + date — two genuinely different reviews from two 
different guests on the same day would look identical in this file by 
construction, so a "duplicate" flag here is structurally ambiguous, 
not necessarily an error. Blindly dropping these rows would silently 
discard real review activity and understate review counts. Option 2 
was rejected because an unverified assumption either way is risky 
given review counts feed directly into demand-proxy analysis (Section 
4.5) and the official Inside Airbnb revenue model (Section 5/6). Option 
3 was chosen because it directly tests the ambiguity using a file that 
actually has the missing context (unique review ID, reviewer ID, 
comment text).

**Finding:** Cross-checked listing_id=193038, date=2015-01-05 (appeared 
3× in reviews.csv) against reviews.csv.gz. Found 3 distinct review IDs, 
3 distinct reviewer IDs, and 3 distinct comment texts — all genuine, 
separate guest reviews left on the same calendar day.

**Decision:** These are NOT duplicate records. No deduplication 
applied. reviews.csv will only be used for review-count aggregation by 
date, never treated as having one row per unique review identity.

**Trade-off accepted:** This investigation only directly verified one 
listing/date combination as a representative sample, not all 27,545 
flagged rows individually (impractical at this scale). We accept the 
reasonable inference that the same structural explanation (multiple 
genuine reviewers, same day) applies across the full flagged set, 
based on the general pattern matching what reviews.csv's column 
structure would predict.

---

## Section 3.1 — availability_365 and number_of_reviews Outlier Check

**Date:** June 20, 2026

**Finding:** availability_365 is correctly bounded (0-365), with no 
invalid values. number_of_reviews ranges 0-5,097, showing strong 
right-skew (median 10, mean 47.8).

**Decision:** No outlier capping or flagging applied to either field. 
availability_365's skew reflects genuine business variation (mostly-
booked vs. mostly-open listings), not data errors. number_of_reviews' 
high max (5,097) represents a legitimate long-running, high-performing 
listing — not an error — consistent with expected power-law dynamics 
in review/booking counts (per Section 4.1 guidance). Both fields will 
be analyzed using their natural distribution; log-scale visualization 
will be used in EDA (Section 4) rather than removing or capping extreme 
values.

---

## Section 3.1 — Geographic Validation

**Date:** June 20, 2026

**Finding:** All 10,480 listings have latitude/longitude within 
Amsterdam's expected bounds (lat 52.29-52.43, long 4.76-5.03). No 
invalid or out-of-bounds coordinates found.

**Decision:** No cleaning or filtering needed for geographic fields.