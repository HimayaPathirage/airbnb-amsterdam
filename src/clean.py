"""
Data cleaning script for Inside Airbnb listings (Amsterdam).
Applies standardization decisions documented in docs/decisions_log.md
"""

import pandas as pd
from pathlib import Path
from ingest import load_listings

PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"


def clean_price(df):
    """Convert price from '$1,234.00' string to numeric float."""
    df['price_clean'] = (
        df['price']
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
        .astype(float)
    )
    return df


def flag_price_outliers(df):
    """Flag confirmed price errors per decisions_log.md (>= €40,000/night)."""
    df['price_outlier_flag'] = df['price_clean'] >= 40000
    return df

def clean_dates(df):
    """Parse date columns from string to datetime."""
    date_cols = ['last_scraped', 'first_review', 'last_review', 'host_since']
    for col in date_cols:
        df[col + '_parsed'] = pd.to_datetime(df[col], errors='coerce')
    return df

def normalize_property_type(df):
    """Group the 60+ raw property_type values into broader categories."""
    def categorize(pt):
        pt_lower = str(pt).lower()
        if 'houseboat' in pt_lower or pt_lower == 'boat':
            return 'Houseboat/Boat'
        elif 'entire' in pt_lower:
            return 'Entire place'
        elif 'private room' in pt_lower:
            return 'Private room'
        elif 'shared room' in pt_lower:
            return 'Shared room'
        elif 'hotel' in pt_lower:
            return 'Hotel room'
        elif pt_lower.startswith('room in'):
            return 'Room in other'
        else:
            return 'Other'

    df['property_type_grouped'] = df['property_type'].apply(categorize)
    return df

def drop_unreliable_columns(df):
    """Drop columns that are 100% null or too unreliable to use."""
    cols_to_drop = ['neighbourhood_group_cleansed', 'calendar_updated', 
                     'host_neighbourhood', 'neighbourhood']
    df = df.drop(columns=cols_to_drop)
    return df


def flag_missing_core_attributes(df):
    """Add explicit missing-value flags for key fields, without imputing fake values."""
    df['beds_missing'] = df['beds'].isnull()
    df['bathrooms_missing'] = df['bathrooms'].isnull()
    df['price_missing'] = df['price_clean'].isnull()
    return df

def standardize_coordinates(df):
    """Round lat/long to a consistent 5 decimal places (~1.1m precision)."""
    df['latitude'] = df['latitude'].round(5)
    df['longitude'] = df['longitude'].round(5)
    return df

def clean_listings():
    df = load_listings()
    df = clean_price(df)
    df = flag_price_outliers(df)
    df = clean_dates(df)
    df = normalize_property_type(df)
    df = drop_unreliable_columns(df)
    df = flag_missing_core_attributes(df)
    df = standardize_coordinates(df)

    print(f"Price cleaned. Outliers flagged: {df['price_outlier_flag'].sum()}")
    
    print(f"\nDate parsing check:")
    print(df[['host_since', 'host_since_parsed']].head(5))
    
    print(f"\nUnparseable dates per column:")
    for col in ['last_scraped', 'first_review', 'last_review', 'host_since']:
        print(f"  {col}: {df[col + '_parsed'].isnull().sum()} unparseable (out of {df[col].notna().sum()} non-null originals)")

    print(f"\nProperty type grouping:")
    print(df['property_type_grouped'].value_counts())
    print(f"\nColumns after dropping unreliable ones: {df.shape[1]}")
    print(f"Missing flags: beds={df['beds_missing'].sum()}, bathrooms={df['bathrooms_missing'].sum()}, price={df['price_missing'].sum()}")

    print(f"\nCoordinate precision after standardization:")
    print(df['latitude'].astype(str).str.split('.').str[1].str.len().value_counts())

    return df

if __name__ == "__main__":
    df_clean = clean_listings()