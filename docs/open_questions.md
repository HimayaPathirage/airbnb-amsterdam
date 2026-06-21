# Open Questions / Deferred Items

Things noticed during the project but deliberately postponed, with 
a plan for when to revisit them.

## 1. host_is_superhost null values (115 listings)
**Found:** Section 3.4, Query 2 result
**Why deferred:** Not blocking current analytical work; small group (115/10,480)
**Plan:** Investigate during Section 4.4 (Host & Supply-Side Analysis) — 
check if these correlate with missing host_response_rate too, and 
decide whether to exclude or footnote them in host-based comparisons.
**Status:** OPEN

## 1. host_is_superhost null values (115 listings) - RESOLVED
**Finding:** 115 listings have null superhost status. Of these, 38 
also lack host_response_rate and 30 lack host_acceptance_rate, but 
all 115 have a valid host_since date. This suggests these are hosts 
with insufficient response/booking history for Airbnb to calculate 
superhost eligibility, not simply incomplete profiles overall.
**Status:** RESOLVED, documented in Section 4.4 notes.

---

**Hypothesis for later investigation (Section 4.4):** The Query 2 
finding (non-superhosts pricing higher than superhosts) may be 
partially explained by property type mix — e.g., superhosts possibly 
concentrated in private-room listings (which individual, responsive 
hosts are more likely to run) vs. commercial entire-place/houseboat 
operators less likely to maintain superhost-qualifying response rates. 
Added to open_questions.md.

## 2. Superhost vs non-superhost pricing gap - RESOLVED
**Finding:** Property type mix fully explains the Section 3.4 finding. 
Non-superhosts are 85.5% Entire place listings (only 7.8% Private 
room), while superhosts are only 46.3% Entire place but 36.7% Private 
room, nearly 5x the share. Since entire-place listings cost 
substantially more than private rooms across the market (Section 3.4 
Query 3), this property-type composition difference, not superhost 
status itself, explains why non-superhosts show a higher average 
price.
**Status:** RESOLVED, documented in Section 4.4 notes.

---

## Section 3.4 — Query 4 Result: Occupancy by Review-Count Bucket

**Finding:** Relationship is non-monotonic, not a simple "more reviews 
= more occupancy" pattern. Occupancy rises from No reviews (0.672) -> 
1-10 reviews (0.782) -> 11-50 reviews (0.800), but then DROPS at 50+ 
reviews (0.593) — lower than even the "No reviews" group.

**Interpretation (preliminary):** This non-monotonic pattern likely 
reflects the known ambiguity in occupancy_rate_calculated (Section 
3.1/3.3 caveat) — "unavailable" conflates genuine bookings with 
host-blocked dates. Listings with 50+ reviews are likely long-
established; their lower calculated occupancy may reflect hosts who 
have scaled back active availability over time, not declining demand. 
This needs deeper investigation in Section 4.5 (Review & Demand-Side 
Analysis) rather than being taken at face value.

**Added to open_questions.md** for follow-up during Section 4.5.

## Resolution: Occupancy Drop at 50+ Reviews (from Section 3.4)

**Investigation:** Checked whether value score or host tenure differ 
meaningfully across review-count buckets to explain the earlier 
finding that occupancy_rate_calculated drops at 50+ reviews despite 
rising through lower buckets.

**Finding:** Value scores are flat across all buckets (4.65-4.66), 
ruling out "guest dissatisfaction" as an explanation. Host tenure does 
increase gradually with review count (8.83 to 9.62 years), consistent 
with more reviews simply requiring more time to accumulate, but this 
increase is modest and does not obviously explain a sharp occupancy 
drop on its own.

**Honest conclusion:** This investigation did not fully resolve the 
non-monotonic occupancy pattern. The most likely remaining explanation, 
based on the original Section 3.1 caveat, is that occupancy_rate_
calculated conflates genuine bookings with host-blocked dates, and 
long-tenured, highly-reviewed hosts may simply be more likely to block 
calendar time for personal use after years of operation. This remains 
a documented limitation rather than a fully solved finding; further 
investigation would require calendar-level booking data not available 
in this dataset.

**Status:** CLOSED (investigated, partial explanation found, residual 
uncertainty documented honestly rather than overstated).