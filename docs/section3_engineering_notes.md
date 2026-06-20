## Section 3.1 — Completeness Assessment

The most frequently missing fields, and their business implications:

1. **neighbourhood_group_cleansed, calendar_updated (100% missing)** — 
   Structurally dead columns for Amsterdam. No implication beyond 
   exclusion from any pipeline.

2. **host_neighbourhood (73.4%), raw neighbourhood (50.5%), 
   neighborhood_overview (50.5%)** — These are host-entered free-text 
   fields. High missingness suggests many hosts skip optional profile 
   details. Implication: any analysis relying on host-self-reported 
   location must use neighbourhood_cleansed instead (Inside Airbnb's 
   standardized, complete version).

3. **price (44.0%) and estimated_revenue_l365d (44.0%)** — Nearly half 
   of listings have no public price. Implication: any price-based 
   market analysis only reflects ~56% of total supply — likely the more 
   "active" half of the market (paused/inactive listings may not 
   display price). This is a meaningful coverage gap that should be 
   stated as a caveat in all pricing conclusions.

4. **beds (43.7%), bathrooms (43.4%)** — Core property attributes 
   missing for a large share of listings. Implication: any "price per 
   bedroom" or capacity-normalized analysis (Section 3.3) will only 
   cover the listings with complete data — sample size will shrink 
   accordingly.

5. **review_scores_* fields (10.5% each)** — Consistent ~10.5% missing 
   across all review score sub-dimensions, matching the ~10.5% of 
   listings with zero reviews (confirmed in Section 2: 1,097 of 10,480 
   listings have no reviews). This is expected and logically consistent 
   — listings cannot have a review score with no reviews.