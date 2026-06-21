## Section 3.1 - Completeness Assessment

The most frequently missing fields, and their business implications:

1. **neighbourhood_group_cleansed, calendar_updated (100% missing)**: 
   Structurally dead columns for Amsterdam. No implication beyond 
   exclusion from any pipeline.

2. **host_neighbourhood (73.4%), raw neighbourhood (50.5%), 
   neighborhood_overview (50.5%)**: These are host-entered free-text 
   fields. High missingness suggests many hosts skip optional profile 
   details. Implication: any analysis relying on host-self-reported 
   location must use neighbourhood_cleansed instead (Inside Airbnb's 
   standardized, complete version).

3. **price (44.0%) and estimated_revenue_l365d (44.0%)**: Nearly half 
   of listings have no public price. Implication: any price-based 
   market analysis only reflects ~56% of total supply, likely the more 
   "active" half of the market (paused/inactive listings may not 
   display price). This is a meaningful coverage gap that should be 
   stated as a caveat in all pricing conclusions.

4. **beds (43.7%), bathrooms (43.4%)**: Core property attributes 
   missing for a large share of listings. Implication: any "price per 
   bedroom" or capacity-normalized analysis (Section 3.3) will only 
   cover the listings with complete data, sample size will shrink 
   accordingly.

5. **review_scores_* fields (10.5% each)**: Consistent ~10.5% missing 
   across all review score sub-dimensions, matching the ~10.5% of 
   listings with zero reviews (confirmed in Section 2: 1,097 of 10,480 
   listings have no reviews). This is expected and logically consistent, 
   listings cannot have a review score with no reviews.

## Section 3.4 - Star Schema Implementation & Validation

**Date:** June 20, 2026

**Implementation:** Built a star schema in PostgreSQL 18 with one fact 
table (fact_listings, grain = one row per listing) and three dimension 
tables (dim_host, dim_neighbourhood, dim_property_type). Loaded via 
Python (psycopg2/SQLAlchemy) directly from the cleaned/enriched 
pandas dataframe using to_sql().

**Validation:**
- Row counts confirmed correct: fact_listings=10,480, dim_host=9,201 
  (fewer than listings, correctly reflecting hosts with multiple 
  properties), dim_neighbourhood=22, dim_property_type=7.
- price_outlier_flag count verified at 7 directly via SQL query, 
  matching the Python-side count exactly.
- 3-table join (fact_listings JOIN dim_host JOIN dim_neighbourhood) 
  executed successfully, confirming foreign key relationships are 
  structurally sound and queryable.

**Tool choice:** PostgreSQL chosen over DuckDB/SQLite due to prior 
hands-on experience (used in an earlier personal project), reducing 
setup risk given the assignment's tight timeline.

## Section 3.4 - Missing Value Flags Gap (Caught During Verification)

**Date:** June 20, 2026

**Finding:** While verifying fact_listings in pgAdmin, discovered that 
price_missing, beds_missing, and bathrooms_missing flags (created in 
Section 3.2) were not included when the table was first built. 
build_fact_listings() only selected price_outlier_flag, omitting the 
three missingness flags despite the decision log stating they would 
be used for analysis.

**Decision:** Updated build_fact_listings() to include all three flags. 
Re-ran load_to_postgres.py (table rebuilt via if_exists='replace'). 
Verified price_missing count in PostgreSQL matches the known value 
(4,606) exactly.

**Lesson:** Demonstrates the importance of verifying actual database 
output against documented decisions, rather than trusting a 
successful script run alone. to_sql() will happily write whatever 
columns are passed to it without warning if intended columns are 
missing.

## Section 3.4 - Query 1 Result: Top Neighbourhoods by Price

Top 5: De Pijp - Rivierenbuurt (€250), Centrum-West (€245.5), 
Centrum-Oost (€240), De Baarsjes - Oud-West (€240), Zuid (€238). 
Notably, De Baarsjes - Oud-West combines the highest listing count 
of all 22 neighbourhoods (1,808) with a top-4 median price, high 
supply and high price coexisting, not a simple inverse relationship.

## Section 3.4 - Query 2 Result: Superhost vs Non-Superhost Pricing

**Finding:** Non-superhosts average €277.07/night (8,496 listings) vs. 
superhosts at €256.15/night (1,862 listings). Non-superhosts price 
HIGHER on average, contrary to the common assumption that superhost 
status correlates with premium pricing. 115 listings have null 
superhost status (average €344.47), not yet investigated.

**Interpretation (preliminary):** Superhost status reflects 
responsiveness/reliability criteria, not luxury positioning, this 
may explain the inverse relationship. Worth deeper investigation in 
Section 4.4 (Host & Supply-Side Analysis), potentially controlling for 
property type or room type as a confounding variable.

## Section 3.4 - Query 3 Result: Price by Property Type

**Finding:** Clear, logical price hierarchy: Houseboat/Boat (€372.93) > 
Entire place (€294.85) > Hotel room (€284.85) > Other (€222.68) > Room 
in other (€171.78) > Private room (€164.36) > Shared room (€113.46). 
Validates that property_type_grouped categorization (Section 3.2) 
produces sensible, differentiated price segments.

**Hypothesis for later investigation (Section 4.4):** The Query 2 
finding (non-superhosts pricing higher than superhosts) may be 
partially explained by property type mix, e.g., superhosts possibly 
concentrated in private-room listings (which individual, responsive 
hosts are more likely to run) vs. commercial entire-place/houseboat 
operators less likely to maintain superhost-qualifying response rates. 
Added to open_questions.md.