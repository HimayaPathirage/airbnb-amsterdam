# Amsterdam Airbnb Market Intelligence

**Data Engineer Intern Technical Assessment**

A complete data engineering and analytics pipeline built on Amsterdam's
Inside Airbnb dataset (10,480 listings): raw data ingestion through to
a PostgreSQL star schema, exploratory analysis, statistical hypothesis
testing, and a 29-page business intelligence report.

**Start here:** [`reports/Amsterdam_Airbnb_Report.pdf`](reports/Amsterdam_Airbnb_Report.pdf)

---

## Tech Stack

Python (pandas, scipy, statsmodels) · PostgreSQL 18 · Jupyter ·
matplotlib / seaborn / folium

---

## Repository Structure

```
airbnb-amsterdam/
├── data/
│   ├── raw/                          # Place downloaded Inside Airbnb files here
│   └── processed/                    # Cleaned/enriched outputs
│
├── notebooks/
│   ├── schema_exploration.ipynb      # Section 2: dataset familiarization
│   ├── cleaning_checks.ipynb         # Section 3.1-3.2: profiling and cleaning verification
│   ├── section4_eda.ipynb            # Section 4: exploratory data analysis
│   └── section5_statistics.ipynb     # Section 5: hypothesis testing and regression
│
├── src/
│   ├── ingest.py                     # Loads raw files from data/raw/
│   ├── profiling.py                  # Generates the data quality report
│   ├── clean.py                      # Price/date cleaning, outlier flagging, normalization
│   ├── enrich.py                     # Joins, occupancy, neighbourhood aggregates, derived fields
│   ├── load_to_postgres.py           # Builds and loads the star schema into PostgreSQL
│   └── queries.sql                   # The 4 analytical SQL queries used in Section 3.4
│
├── reports/
│   ├── Amsterdam_Airbnb_Report.pdf   # The final report, read this first
│   ├── listing_density_map.html      # Interactive choropleth, listing density by neighbourhood
│   ├── review_score_map.html         # Interactive choropleth, review scores by neighbourhood
│   └── *.png                         # 11 static figures (price, ratings, geography, regression)
│
├── docs/
│   ├── decisions_log.md              # Full engineering decision trail (options, reasoning, trade-offs)
│   ├── data_model.md                 # Star schema design and modeling trade-offs
│   ├── data_quality_report.md        # Automated profiling output (nulls, duplicates, dtypes)
│   ├── open_questions.md             # Findings flagged, investigated, and resolved mid-project
│   ├── section2_dataset_notes.md     # Section 2 schema, limitations, assumptions, domain context
│   ├── section3_engineering_notes.md # Section 3 engineering findings
│   ├── section4_eda_note.md          # Section 4 EDA findings and business interpretations
│   └── section5_statistics_note.md   # Section 5 hypothesis test write-ups
│
├── .env                              # Local-only database password (not committed)
├── .gitignore
└── README.md
```

---

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy statsmodels psycopg2-binary sqlalchemy folium python-dotenv
   ```
2. Download the Amsterdam dataset from [Inside Airbnb](https://insideairbnb.com/get-the-data/)
   and place all 7 files into `data/raw/`.
3. Create a `.env` file in the project root with your own PostgreSQL
   password:
   ```
   DB_PASSWORD=your_actual_password
   ```
4. Run the pipeline in order:
   ```bash
   python src/ingest.py
   python src/profiling.py
   python src/clean.py
   python src/enrich.py
   python src/load_to_postgres.py
   ```
5. Open the notebooks in `notebooks/` (in the order listed above) in
   Jupyter to reproduce the analysis, charts, and statistical tests.
6. Run the 4 analytical SQL queries in `src/queries.sql` against the
   loaded database using pgAdmin or psql.
7. Open `reports/listing_density_map.html` and
   `reports/review_score_map.html` directly in a browser for the
   interactive versions of Figures 5 and 7.

---

## Recommended Review Order

| Order | What | Why |
|---|---|---|
| 1 | `reports/Amsterdam_Airbnb_Report.pdf` | The complete write-up: findings, recommendations, limitations, and the AI usage disclosure (Appendix A) |
| 2 | `reports/listing_density_map.html`, `review_score_map.html` | Interactive versions of two key geographic findings |
| 3 | `docs/decisions_log.md` | The full engineering decision trail referenced throughout the report |
| 4 | `docs/section2_dataset_notes.md` → `section5_statistics_note.md` | Detailed working notes behind each report section |
| 5 | `src/` | Pipeline source code, run in the order listed above |
| 6 | `notebooks/` | The exploratory and statistical analysis as actually run |
| 7 | `docs/data_model.md`, `data_quality_report.md` | Star schema design and automated data profiling |
| 8 | `docs/open_questions.md` | Transparent log of findings investigated mid-project |

---

## Summary of Completed Work

Sections 2 through 5 of the assignment brief were completed in full:

- **Dataset Familiarization**: full schema documentation, relationship
  mapping, limitations, and assumptions for all 7 source files
- **Data Engineering**: cleaning, outlier detection (7 confirmed price
  errors flagged via name-level investigation), enrichment, and a
  PostgreSQL star schema (1 fact table, 3 dimension tables, 4 validated
  analytical queries)
- **EDA**: 10 figures across price distributions, geography, time
  trends, host behavior, and review patterns, each with business
  interpretation
- **Statistical Analysis**: 5 hypotheses tested with appropriate
  non-parametric methods (Mann-Whitney U, Kruskal-Wallis), effect
  sizes, confidence intervals, and a regression with VIF and LOWESS
  diagnostics

See Section 2.3 of the report for full prioritization rationale.

## Summary of Incomplete Work

Optional Sections 6 (Data Science), 7 (AI/ML Experimentation), and 8
(Open Innovation) were not attempted. See Section 13.3 of the report
for the reasoning behind this scope decision.

---

## Credentials Notice

No credentials, API keys, or personal data are included in this
repository. The `.env` file referenced above is excluded via
`.gitignore` and must be created locally with your own PostgreSQL
password before running `load_to_postgres.py`.

---

## AI Usage Disclosure

AI assistance (Claude, Anthropic) was used throughout this project as
a learning and development aid. Full disclosure, including what was
AI-assisted, what was independently verified, and where AI suggestions
were challenged or corrected, is documented in **Appendix A** of the
final report.