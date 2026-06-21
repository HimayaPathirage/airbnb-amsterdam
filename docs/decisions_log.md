# Assumptions & Decisions Log

## Section 2/3 - Calendar Data Price Field

**Date:** June 19, 2026
**Finding:** `calendar.csv.gz` price/adjusted_price fields are 100% null for 
Amsterdam (all 3.8M rows).

**Decision:** Cannot compute per-day revenue from calendar data as originally 
planned. Will instead use `listings.csv.gz`'s `price` field (static, current 
price) combined with `estimated_occupancy_l365d` and `estimated_revenue_l365d`, 
which Inside Airbnb already provides pre-calculated, for revenue-related 
analysis. Calendar's `available` field remains usable for occupancy-rate 
calculations.

**Trade-off accepted:** Revenue estimates rely on Inside Airbnb's own 
pre-computed methodology rather than a custom calculation, so we inherit 
whatever assumptions they used (not transparent to us).

## Section 3.1 - Price Outlier Threshold Decision (Final)

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
   genuine errors vs. real (if extreme) listings, then flag, not 
   delete, the confirmed errors. (CHOSEN)

**Why this approach:** Option 1 was rejected because the magnitude of 
distortion is severe. A single €80,018 row can shift a mean for 5,874 
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
night), too broad to be useful on its own. Inspected the full price 
distribution above €2,000 to find a natural break point, combined with 
manual name-based verification of the most extreme listings.

**Finding:** Prices form a continuous, plausible distribution up to 
~€2,975 (round-number clustering at €500 suggests deliberate host 
pricing, not errors). A moderate, unconfirmed jump occurs at 
€3,930-€13,978 (6 listings). A clear, severe break occurs at €40,000+ 
(7 listings), independently confirmed via listing names as data entry 
errors or test listings (e.g., two "Havenlodge" listings at €80,018/
night for 4 guests, multiple "Hotel room"-style listings at 
€40,000-€50,000 for 2-6 guests, and one listing literally named 
"test host, don't book").

**Decision:** 
- Listings priced >= €40,000/night (7 listings) flagged via a new 
  boolean column `price_outlier_flag = True` and excluded from all 
  price-based statistics, distributions, and modeling.
- Listings priced €3,930-€13,978 (6 listings) kept but visually 
  reviewed in EDA, flagged in commentary only, not excluded.
- Raw price column never modified; flag is additive.

**Trade-off accepted:** A hard cutoff at exactly €40,000 is somewhat 
arbitrary at the boundary, but justified by the combination of a 
visible statistical gap and independent name-based confirmation. We 
accept the small risk that 1-2 borderline rows near the cutoff could 
be misclassified in either direction.

**Correction (June 20):** Original entry stated 5 listings at the 
€40,000+ threshold; verified count via clean.py implementation is 
actually 7 listings. Text corrected, threshold and reasoning unchanged.

---

## Section 3.1 - reviews.csv "Duplicate" Investigation

**Date:** June 20, 2026

**Options considered:**
1. Automatically drop all 27,545 rows flagged as exact-match duplicates 
   by the profiling script.
2. Ignore the duplicate flag entirely and proceed without checking.
3. Cross-reference flagged rows against the detailed reviews.csv.gz 
   file (which has unique review IDs) before deciding. (CHOSEN)

**Why this approach:** Option 1 was rejected because reviews.csv only 
contains listing_id + date. Two genuinely different reviews from two 
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
3x in reviews.csv) against reviews.csv.gz. Found 3 distinct review IDs, 
3 distinct reviewer IDs, and 3 distinct comment texts, all genuine, 
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

## Section 3.1 - availability_365 and number_of_reviews Outlier Check

**Date:** June 20, 2026

**Finding:** availability_365 is correctly bounded (0-365), with no 
invalid values. number_of_reviews ranges 0-5,097, showing strong 
right-skew (median 10, mean 47.8).

**Decision:** No outlier capping or flagging applied to either field. 
availability_365's skew reflects genuine business variation (mostly-
booked vs. mostly-open listings), not data errors. number_of_reviews' 
high max (5,097) represents a legitimate long-running, high-performing 
listing, not an error, consistent with expected power-law dynamics 
in review/booking counts (per Section 4.1 guidance). Both fields will 
be analyzed using their natural distribution; log-scale visualization 
will be used in EDA (Section 4) rather than removing or capping extreme 
values.

---

## Section 3.1 - Geographic Validation

**Date:** June 20, 2026

**Finding:** All 10,480 listings have latitude/longitude within 
Amsterdam's expected bounds (lat 52.29-52.43, long 4.76-5.03). No 
invalid or out-of-bounds coordinates found.

**Decision:** No cleaning or filtering needed for geographic fields.

## Section 3.2 - Date Parsing Verification

**Date:** June 20, 2026

**Finding:** Parsed last_scraped, first_review, last_review, and 
host_since to proper datetime format. first_review/last_review nulls 
(1,097) confirmed to exactly match the known count of listings with 
zero reviews, not a parsing issue. host_since nulls (3) confirmed to 
be genuinely null in raw data, not malformed text. 0 actual parsing 
failures across all 4 date columns.

**Decision:** No further action needed; all date fields parse cleanly.

## Section 3.2 - Property Type Normalization

**Date:** June 20, 2026

**Options considered:**
1. Use the raw property_type field as-is (63 unique values) for any 
   grouped analysis.
2. Use only room_type (4 clean categories) and ignore property_type 
   entirely.
3. Build a custom grouping function to collapse property_type into a 
   manageable number of categories, preserving meaningful Amsterdam-
   specific segments. (CHOSEN)

**Why this approach:** Option 1 was rejected; 63 categories is too 
granular for most aggregate analysis (e.g., price-by-property-type 
charts would be unreadable). Option 2 was rejected because room_type 
alone loses meaningful distinctions, e.g., houseboats and hotel rooms 
are not captured at all by room_type's 4 categories, despite being 
significant segments in Amsterdam's market (392 houseboats/boats, 418 
hotel-style rooms). Option 3 was chosen to preserve this signal while 
still reducing complexity to a manageable number of groups.

**Finding:** An initial keyword-based grouping (entire/private/shared/
hotel only) produced an "Other" bucket of 364 listings (3.5%), which on 
inspection contained 308 houseboats/boats, a significant, Amsterdam-
specific accommodation type, not a rare edge case. Refined the function 
to add dedicated "Houseboat/Boat" and "Room in other" categories, 
reducing "Other" to 30 listings (0.3%) containing only genuine rare 
one-offs (Tiny home, Tent, Yurt, Cave, etc.).

**Decision:** New column `property_type_grouped` created with 7 
categories: Entire place, Private room, Hotel room, Houseboat/Boat, 
Shared room, Room in other, Other. Original property_type column 
preserved unchanged.

**Note:** property_type_grouped's "Hotel room" count (418) differs from 
room_type's "Hotel room" count (49); these measure different things. 
room_type reflects Inside Airbnb's stricter booking-type classification; 
property_type_grouped reflects the host's self-described property 
style. Both fields will be retained for different analytical purposes.

## Section 3.2 - Missing Value Handling

**Date:** June 20, 2026

**Decision:** Dropped 4 unreliable/dead columns (neighbourhood_group_cleansed, 
calendar_updated, host_neighbourhood, neighbourhood; all either 100% 
null or too unreliable per Section 2 assumptions). For remaining 
high-null fields (beds, bathrooms, price), chose explicit-null strategy 
over imputation, with added boolean flag columns (beds_missing, 
bathrooms_missing, price_missing) so missingness itself remains a 
visible, analyzable signal rather than being silently filled with 
potentially misleading values.

**Verification:** Flag counts confirmed against Section 3.1 profiling: 
beds_missing=4576 (43.7%), bathrooms_missing=4548 (43.4%), 
price_missing=4606 (44.0%), all match exactly.

**Trade-off accepted:** Explicit nulls mean any aggregate price/bedroom 
statistic will be computed on a reduced sample (~56-57% of listings), 
not the full dataset. This is preferable to imputation, which would 
risk fabricating systematic bias (e.g., imputing mean price would 
understate true price variance).

## Section 3.2 - Domain Validation Rules

**Date:** June 20, 2026

**Rules checked:**
1. price_clean >= 0
2. accommodates >= 1
3. minimum_nights >= 1
4. host_since_parsed <= last_scraped_parsed (host cannot join after 
   the scrape date)
5. latitude/longitude within Amsterdam bounds (verified separately in 
   Section 3.1, 0 violations)

**Finding:** Zero violations across all 5 rules, out of 10,480 rows.

**Decision:** No records removed or flagged for domain-rule violations. 
This dataset shows strong structural integrity on basic logical 
constraints. The data quality issues found elsewhere (missing prices, 
extreme outliers) are about completeness and statistical extremity, 
not logical impossibility.

## Section 3.2 - Geographic Field Standardization

**Date:** June 20, 2026

**Finding:** Neighbourhood names already verified clean (22/22 exact 
match across files, Section 2). Latitude/longitude values had 
inconsistent decimal precision (ranging 1-16 decimal places, likely 
floating-point artifacts), though all were already within valid 
Amsterdam bounds (Section 3.1).

**Decision:** Rounded latitude/longitude to a consistent 5 decimal 
places (~1.1m precision) using `.round(5)`. Verified via 
`.round(5).equals()` that all values are correctly standardized. No 
city-name standardization needed (single-city dataset).

**Trade-off accepted:** 5 decimal places sacrifices sub-meter precision 
that some raw values technically had, but this level of precision 
provides no meaningful analytical benefit and adds noise/inconsistency 
instead.

## Section 3.3 - Review Count Cross-Validation

**Date:** June 20, 2026

**Finding:** Computed review counts independently from reviews.csv 
(grouping by listing_id) and compared against listings.csv.gz's 
pre-existing number_of_reviews column. Result: 0 mismatches across all 
10,480 listings, perfect agreement.

**Decision:** This confirms strong internal consistency between the 
two files. number_of_reviews can be trusted as accurate; 
review_count_computed serves primarily as a validation artifact and 
will be dropped from the final enriched table to avoid redundant 
columns (unless needed later for date-filtered review counts, e.g., 
"reviews in the last 90 days," which would require a fresh groupby on 
a filtered reviews.csv).

## Section 3.3 - Occupancy Rate Calculation

**Date:** June 20, 2026

**Method:** Computed occupancy_rate_calculated per listing as the 
proportion of calendar days marked unavailable ('f') out of all 365 
days in calendar.csv.gz.

**Finding:** Mean occupancy rate 74.2%, consistent with the overall 
unavailable-day proportion found in Section 3.1 (74.2% of all 3.8M 
listing-days). Median 94.5% but 25th percentile only 52.6%, 
distribution is left-skewed toward high "occupancy."

**Caveat (per Section 3.1 data dictionary finding):** This metric 
cannot distinguish between genuinely booked days and host-blocked 
days. A listing showing 100% "occupancy" may simply have a host who 
manually closed their calendar rather than one that is fully booked by 
guests. This will be explicitly stated wherever occupancy_rate_calculated 
is used in EDA or reporting; it is a proxy for unavailability, not 
confirmed bookings.

**Decision:** Retain as occupancy_rate_calculated (not renamed to 
"booking rate" or similar, to keep the ambiguity visible in the column 
name itself).

## Section 3.3 - Neighbourhood-Level Aggregates

**Date:** June 20, 2026

**Method:** Grouped listings by neighbourhood_cleansed, computed median 
price, listing count, and average review rating per neighbourhood, 
merged back onto every listing row.

**Finding:** Median prices range €169-€250 across neighbourhoods 
(sample), with no invalid values. Listing counts range 125-1,207, 
confirming real density variation (Centrum-West, De Pijp - 
Rivierenbuurt are most saturated). Average ratings are tightly 
clustered (4.80-4.88) with little neighbourhood-level variation, an 
early indication of the rating-inflation pattern that Section 4.1 EDA 
will investigate formally.

**Decision:** Retain all three aggregate columns 
(neighbourhood_median_price, neighbourhood_listing_count, 
neighbourhood_avg_rating) as enrichment features for downstream EDA 
and modeling (e.g., comparing a listing's own price to its 
neighbourhood's median).

## Section 3.3 - Derived Field Corrections (price_per_bedroom, review_frequency)

**Date:** June 20, 2026

**Issue found:** price_per_bedroom initially leaked confirmed price 
errors (the 7 listings flagged >=€40,000/night) straight through, 
producing values up to €80,018/bedroom.

**Fix:** Applied price_outlier_flag exclusion before computing 
price_per_bedroom. Max dropped to €11,000/bedroom, this is one of the 
6 "borderline high but unconfirmed" listings from the €3,930-€13,978 
range (Section 3.1 decision), correctly passing through since that 
range was deliberately not excluded, only flagged for EDA-stage review.

**Issue investigated:** review_frequency showed a max of 1,201 
reviews/year. Initially suspected a tenure-floor calculation issue; 
added a 30-day minimum tenure threshold as a guard.

**Finding:** The extreme value traced to listing 50383849: 
host_tenure_years=4.24 (well above the 30-day floor), 
review_count_computed=5,097, the same listing previously identified 
in Section 3.1 as having the dataset's maximum review count. This is 
the same legitimate high-volume listing, not a tenure-calculation 
artifact. The 30-day floor fix was correctly implemented but was never 
going to resolve this specific case, since it solves a different 
problem (new hosts with near-zero tenure).

**Decision:** No further capping applied to review_frequency. Consistent 
with the Section 3.1 decision on number_of_reviews, this is treated as 
genuine right-skewed business variation (a high-turnover listing), not 
a data error. Will be visualized on a log scale in EDA rather than 
excluded or capped.