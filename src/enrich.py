"""
Data enrichment script for Inside Airbnb listings (Amsterdam).
Joins listings with calendar-derived occupancy and review aggregates.
"""

import pandas as pd
from pathlib import Path
from ingest import load_calendar, load_reviews_summary
from clean import clean_listings


def add_review_counts(df_listings, df_reviews):
    """Add a fresh review count per listing, computed directly from reviews.csv."""
    review_counts = df_reviews.groupby('listing_id').size().reset_index(name='review_count_computed')
    df = df_listings.merge(review_counts, left_on='id', right_on='listing_id', how='left')
    df['review_count_computed'] = df['review_count_computed'].fillna(0)
    df = df.drop(columns=['listing_id'])
    return df

def add_occupancy_rate(df_listings, df_calendar):
    """Compute occupancy rate per listing: % of days marked unavailable (booked)."""
    occupancy = df_calendar.groupby('listing_id')['available'].apply(
        lambda x: (x == 'f').sum() / len(x)
    ).reset_index(name='occupancy_rate_calculated')
    
    df = df_listings.merge(occupancy, left_on='id', right_on='listing_id', how='left')
    df = df.drop(columns=['listing_id'])
    return df

def add_neighbourhood_aggregates(df):
    """Compute neighbourhood-level stats and merge back onto each listing."""
    agg = df.groupby('neighbourhood_cleansed').agg(
        neighbourhood_median_price=('price_clean', 'median'),
        neighbourhood_listing_count=('id', 'count'),
        neighbourhood_avg_rating=('review_scores_rating', 'mean')
    ).reset_index()

    df = df.merge(agg, on='neighbourhood_cleansed', how='left')
    return df

import numpy as np

def add_derived_fields(df):
    """Add host tenure, review frequency, and price-per-bedroom."""
    reference_date = df['last_scraped_parsed'].max()
    
    df['host_tenure_years'] = (
        (reference_date - df['host_since_parsed']).dt.days / 365.25
    )
    
    safe_tenure = df['host_tenure_years'].where(df['host_tenure_years'] >= (30/365.25), np.nan)
    df['review_frequency'] = df['review_count_computed'] / safe_tenure
    
    # Exclude confirmed price errors before computing price_per_bedroom
    safe_price = df['price_clean'].where(df['price_outlier_flag'] == False, np.nan)
    safe_bedrooms = df['bedrooms'].replace(0, np.nan)
    df['price_per_bedroom'] = (safe_price / safe_bedrooms).astype(float)
    
    return df

def enrich_listings():
    df_listings = clean_listings()
    df_reviews = load_reviews_summary()
    df_calendar = load_calendar()

    df = add_review_counts(df_listings, df_reviews)
    df = add_occupancy_rate(df, df_calendar)
    df = add_neighbourhood_aggregates(df)
    df = add_derived_fields(df)

    print(f"Enriched listings shape: {df.shape}")
    print(df[['id', 'number_of_reviews', 'review_count_computed']].head(10))
    mismatch = (df['number_of_reviews'] != df['review_count_computed']).sum()
    print(f"\nRows where number_of_reviews != review_count_computed: {mismatch}")
    
    print(f"\nOccupancy rate stats:")
    print(df['occupancy_rate_calculated'].describe())

    print(f"\nNeighbourhood aggregates (sample):")
    print(df[['neighbourhood_cleansed', 'neighbourhood_median_price', 
               'neighbourhood_listing_count', 'neighbourhood_avg_rating']].drop_duplicates().head(10))
    
    print(f"\nDerived fields sample:")
    print(df[['host_tenure_years', 'review_frequency', 'price_per_bedroom']].describe())

    return df

if __name__ == "__main__":
    df_enriched = enrich_listings()