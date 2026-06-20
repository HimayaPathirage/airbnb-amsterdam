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

**Hypothesis for later investigation (Section 4.4):** The Query 2 
finding (non-superhosts pricing higher than superhosts) may be 
partially explained by property type mix — e.g., superhosts possibly 
concentrated in private-room listings (which individual, responsive 
hosts are more likely to run) vs. commercial entire-place/houseboat 
operators less likely to maintain superhost-qualifying response rates. 
Added to open_questions.md.

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

## 1. host_is_superhost null values (115 listings) - RESOLVED
**Finding:** 115 listings have null superhost status. Of these, 38 
also lack host_response_rate and 30 lack host_acceptance_rate, but 
all 115 have a valid host_since date. This suggests these are hosts 
with insufficient response/booking history for Airbnb to calculate 
superhost eligibility, not simply incomplete profiles overall.
**Status:** RESOLVED, documented in Section 4.4 notes.

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