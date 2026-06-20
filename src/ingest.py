"""
Ingestion script for Inside Airbnb data (Amsterdam).
Loads raw files from data/raw/ and reports basic profiling info.
"""

import pandas as pd
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"


def load_listings():
    path = RAW_DIR / "listings.csv.gz"
    df = pd.read_csv(path, compression='gzip')
    print(f"Loaded listings: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def load_calendar():
    path = RAW_DIR / "calendar.csv.gz"
    df = pd.read_csv(path, compression='gzip')
    print(f"Loaded calendar: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def load_reviews_summary():
    path = RAW_DIR / "reviews.csv"
    df = pd.read_csv(path)
    print(f"Loaded reviews summary: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def load_neighbourhoods():
    path = RAW_DIR / "neighbourhoods.csv"
    df = pd.read_csv(path)
    print(f"Loaded neighbourhoods: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


if __name__ == "__main__":
    df_listings = load_listings()
    df_calendar = load_calendar()
    df_reviews = load_reviews_summary()
    df_neighbourhoods = load_neighbourhoods()