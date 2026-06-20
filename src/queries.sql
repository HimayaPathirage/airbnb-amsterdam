-- ============================================
-- Section 3.4: Analytical SQL Queries
-- Amsterdam Inside Airbnb Star Schema
-- ============================================

-- Query 1: Top 5 neighbourhoods by median price
SELECT neighbourhood_cleansed, neighbourhood_median_price, neighbourhood_listing_count
FROM dim_neighbourhood
ORDER BY neighbourhood_median_price DESC
LIMIT 5;


-- Query 2: Superhost vs non-superhost average price
SELECT h.host_is_superhost, 
       ROUND(AVG(f.price_clean)::numeric, 2) AS avg_price,
       COUNT(*) AS listing_count
FROM fact_listings f
JOIN dim_host h ON f.host_id = h.host_id
WHERE f.price_outlier_flag = false
GROUP BY h.host_is_superhost;


-- Query 3: Average price by property type
SELECT property_type_grouped, 
       ROUND(AVG(price_clean)::numeric, 2) AS avg_price,
       COUNT(*) AS listing_count
FROM fact_listings
WHERE price_outlier_flag = false
GROUP BY property_type_grouped
ORDER BY avg_price DESC;


-- Query 4: Occupancy rate by review-count bucket
SELECT 
    CASE 
        WHEN review_count_computed = 0 THEN 'No reviews'
        WHEN review_count_computed BETWEEN 1 AND 10 THEN '1-10 reviews'
        WHEN review_count_computed BETWEEN 11 AND 50 THEN '11-50 reviews'
        ELSE '50+ reviews'
    END AS review_bucket,
    ROUND(AVG(occupancy_rate_calculated)::numeric, 3) AS avg_occupancy,
    COUNT(*) AS listing_count
FROM fact_listings
GROUP BY review_bucket
ORDER BY avg_occupancy DESC;