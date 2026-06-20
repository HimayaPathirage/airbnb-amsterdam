"""
Data quality profiling for Inside Airbnb data (Amsterdam).
Generates a summary report across all ingested files.
"""

import pandas as pd
from pathlib import Path
from ingest import load_listings, load_calendar, load_reviews_summary, load_neighbourhoods

REPORT_PATH = Path(__file__).parent.parent / "docs" / "data_quality_report.md"


def profile_dataframe(df, name):
    """Returns a profiling summary dict for one dataframe."""
    null_pct = (df.isnull().mean() * 100).round(1)
    return {
        "name": name,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "duplicate_rows": df.duplicated().sum(),
        "null_summary": null_pct[null_pct > 0].sort_values(ascending=False),
    }


def write_report(profiles):
    lines = ["# Data Quality Report — Amsterdam Inside Airbnb\n"]
    for p in profiles:
        lines.append(f"## {p['name']}")
        lines.append(f"- Rows: {p['rows']}")
        lines.append(f"- Columns: {p['columns']}")
        lines.append(f"- Duplicate rows: {p['duplicate_rows']}")
        lines.append(f"- Columns with missing values:")
        if len(p['null_summary']) == 0:
            lines.append("  - None")
        else:
            for col, pct in p['null_summary'].items():
                lines.append(f"  - {col}: {pct}%")
        lines.append("")
    REPORT_PATH.write_text("\n".join(lines))
    print(f"Report written to {REPORT_PATH}")


if __name__ == "__main__":
    df_listings = load_listings()
    df_calendar = load_calendar()
    df_reviews = load_reviews_summary()
    df_neighbourhoods = load_neighbourhoods()

    profiles = [
        profile_dataframe(df_listings, "listings.csv.gz"),
        profile_dataframe(df_calendar, "calendar.csv.gz"),
        profile_dataframe(df_reviews, "reviews.csv"),
        profile_dataframe(df_neighbourhoods, "neighbourhoods.csv"),
    ]

    write_report(profiles)