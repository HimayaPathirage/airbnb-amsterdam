# Amsterdam Airbnb Market Intelligence
## Data Engineer Intern Technical Assessment - Expernetic

## Overview
This repository contains a complete data engineering and analytics
pipeline for Amsterdam's Inside Airbnb dataset (10,480 listings), built
for the Data Engineer Intern technical assessment.

## Repository Structure
```
airbnb-amsterdam/
├── data/
│   ├── raw/          # Place downloaded Inside Airbnb files here
│   └── processed/    # Cleaned/enriched outputs
├── notebooks/        # EDA and statistical analysis notebooks
├── src/               # Pipeline scripts (ingest, clean, enrich, load)
├── reports/           # Final PDF report and chart figures
└── docs/              # Decisions log, data model, data quality report
```

## How to Run

1. Install dependencies:
   ```
   pip install pandas numpy matplotlib seaborn scipy statsmodels psycopg2-binary sqlalchemy folium
   ```
2. Download the Amsterdam dataset from Inside Airbnb and place all 7
   files into `data/raw/`.
3. Run the pipeline in order:
   ```
   python src/ingest.py
   python src/profiling.py
   python src/clean.py
   python src/enrich.py
   python src/load_to_postgres.py
   ```
   (Update the PostgreSQL connection string in `load_to_postgres.py`
   with your own credentials before running.)
4. Open `notebooks/01_schema_exploration.ipynb`, `02_eda.ipynb`, and
   `03_statistics.ipynb` in Jupyter to reproduce the analysis and charts.

## Recommended Review Order

1. **`reports/Amsterdam_Airbnb_Report.pdf`** - start here, the complete
   write-up with all findings, recommendations, and the AI usage
   disclosure (Appendix A).
2. **`docs/decisions_log.md`** - the full engineering decision trail
   referenced throughout the report.
3. **`src/`** - pipeline source code.
4. **`notebooks/`** - exploratory and statistical analysis.
5. **`docs/data_model.md`** - star schema design and trade-offs.
6. **`docs/data_quality_report.md`** - automated profiling output.

## Summary of Completed Work
Sections 2 through 5 of the assignment brief (Dataset Familiarization,
Data Engineering, EDA, Statistical Analysis) were completed in full.
See Section 2.3 of the report for prioritization rationale.

## Summary of Incomplete Work
Optional Sections 6 (Data Science), 7 (AI/ML Experimentation), and 8
(Open Innovation) were not attempted; see Section 13.3 of the report
for the reasoning behind this scope decision.

## Credentials Notice
No credentials, API keys, or personal data are included in this
repository. The PostgreSQL connection string in `load_to_postgres.py`
must be filled in locally and should never be committed with real
credentials.