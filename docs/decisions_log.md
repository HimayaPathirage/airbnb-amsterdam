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