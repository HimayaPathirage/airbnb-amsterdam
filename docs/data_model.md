# Data Model — Star Schema

## Fact Table: fact_listings
**Grain:** One row per listing
**Primary Key:** listing_id

| Column | Type | Description |
|---|---|---|
| listing_id | INTEGER (PK) | Unique listing identifier |
| host_id | INTEGER (FK -> dim_host) | Host who owns this listing |
| neighbourhood_cleansed | TEXT (FK -> dim_neighbourhood) | Neighbourhood |
| property_type_grouped | TEXT (FK -> dim_property_type) | Grouped property type |
| price_clean | FLOAT | Nightly price (cleaned) |
| price_outlier_flag | BOOLEAN | True if confirmed price error |
| occupancy_rate_calculated | FLOAT | Proportion of unavailable days |
| review_count_computed | INTEGER | Total reviews |
| review_frequency | FLOAT | Reviews per year of host tenure |
| price_per_bedroom | FLOAT | Price / bedrooms (outliers excluded) |
| estimated_revenue_l365d | FLOAT | Inside Airbnb's modeled revenue estimate |
| host_tenure_years | FLOAT | Years since host joined |

## Dimension: dim_host
**Grain:** One row per host
**Primary Key:** host_id

| Column | Type | Description |
|---|---|---|
| host_id | INTEGER (PK) | Unique host identifier |
| host_name | TEXT | Host's display name |
| host_since | DATE | Date host joined platform |
| host_is_superhost | BOOLEAN | Superhost status |
| host_response_rate | TEXT | Self-reported response rate |
| calculated_host_listings_count | INTEGER | Host's total listing count |

## Dimension: dim_neighbourhood
**Grain:** One row per neighbourhood
**Primary Key:** neighbourhood_cleansed

| Column | Type | Description |
|---|---|---|
| neighbourhood_cleansed | TEXT (PK) | Neighbourhood name |
| neighbourhood_median_price | FLOAT | Median price across listings |
| neighbourhood_listing_count | INTEGER | Total listings in this area |
| neighbourhood_avg_rating | FLOAT | Average review rating |

## Dimension: dim_property_type
**Grain:** One row per grouped property type
**Primary Key:** property_type_grouped

| Column | Type | Description |
|---|---|---|
| property_type_grouped | TEXT (PK) | Entire place / Private room / etc. |

## Relationships
- fact_listings.host_id -> dim_host.host_id (many-to-one)
- fact_listings.neighbourhood_cleansed -> dim_neighbourhood.neighbourhood_cleansed (many-to-one)
- fact_listings.property_type_grouped -> dim_property_type.property_type_grouped (many-to-one)

## Modeling Trade-offs

1. **Denormalization in dim_neighbourhood:** Pre-computed aggregates 
   (median price, listing count, avg rating) trade query speed for 
   staleness risk — these values are a snapshot, not live-recalculated.

2. **No Slowly Changing Dimension (SCD) handling:** dim_host uses 
   SCD Type 1 (always-current, no history) rather than Type 2. 
   Appropriate given Inside Airbnb itself is a single-snapshot 
   dataset, not a continuous feed — there is no historical host data 
   to preserve in the first place.

3. **Listing-grain fact table only:** Chose not to build a second, 
   much larger calendar-grain fact table (3.8M rows) given the 
   project timeline. This means date-level questions (e.g., seasonal 
   occupancy patterns) require falling back to pandas rather than 
   pure SQL — a deliberate scope trade-off, not an oversight.

4. **PostgreSQL over DuckDB/SQLite:** Chose based on prior hands-on 
   experience to reduce setup risk, accepting the added overhead of 
   server/connection management compared to a zero-setup embedded 
   engine like DuckDB.