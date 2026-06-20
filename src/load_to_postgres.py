"""
Loads the cleaned/enriched dataset into PostgreSQL as a star schema:
fact_listings, dim_host, dim_neighbourhood, dim_property_type
"""

import pandas as pd
from sqlalchemy import create_engine
from enrich import enrich_listings

# Update the password below to match what you used for postgres
DB_CONNECTION = "postgresql://postgres:postgres123@localhost:5432/airbnb_amsterdam"


def build_dim_host(df):
    dim_host = df[['host_id', 'host_name', 'host_since', 'host_is_superhost',
                    'host_response_rate', 'calculated_host_listings_count']].drop_duplicates(subset='host_id')
    return dim_host


def build_dim_neighbourhood(df):
    dim_neighbourhood = df[['neighbourhood_cleansed', 'neighbourhood_median_price',
                             'neighbourhood_listing_count', 'neighbourhood_avg_rating']].drop_duplicates(subset='neighbourhood_cleansed')
    return dim_neighbourhood


def build_dim_property_type(df):
    dim_property_type = df[['property_type_grouped']].drop_duplicates()
    return dim_property_type


def build_fact_listings(df):
    fact_cols = ['id', 'host_id', 'neighbourhood_cleansed', 'property_type_grouped',
                 'price_clean', 'price_outlier_flag', 'price_missing',
                 'beds_missing', 'bathrooms_missing',
                 'occupancy_rate_calculated', 'review_count_computed', 
                 'review_frequency', 'price_per_bedroom',
                 'estimated_revenue_l365d', 'host_tenure_years']
    fact_listings = df[fact_cols].rename(columns={'id': 'listing_id'})
    return fact_listings


def load_all():
    df = enrich_listings()
    engine = create_engine(DB_CONNECTION)

    dim_host = build_dim_host(df)
    dim_neighbourhood = build_dim_neighbourhood(df)
    dim_property_type = build_dim_property_type(df)
    fact_listings = build_fact_listings(df)

    dim_host.to_sql('dim_host', engine, if_exists='replace', index=False)
    dim_neighbourhood.to_sql('dim_neighbourhood', engine, if_exists='replace', index=False)
    dim_property_type.to_sql('dim_property_type', engine, if_exists='replace', index=False)
    fact_listings.to_sql('fact_listings', engine, if_exists='replace', index=False)

    print("All tables loaded successfully.")
    print(f"dim_host: {len(dim_host)} rows")
    print(f"dim_neighbourhood: {len(dim_neighbourhood)} rows")
    print(f"dim_property_type: {len(dim_property_type)} rows")
    print(f"fact_listings: {len(fact_listings)} rows")


if __name__ == "__main__":
    load_all()