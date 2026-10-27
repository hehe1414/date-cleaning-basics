# Date Cleaning Basics — Task 27

**Track:** Data Analytics | **Organization:** Veda Technology | **Level/Day:** Level 1 — Day 27

## Objective
Standardize inconsistent date formats, identify missing or invalid dates, and document data-quality issues.

## Files
- `retail_sales_messy_dates.csv` — sample input with mixed formats and intentional issues.
- `clean_dates.py` — reusable Pandas cleaning script.
- `cleaned_retail_sales.csv` — original data plus `Clean_Date` and `Issue` columns.
- `date_issue_log.csv` — issue log including invalid/missing dates and format changes.
- `cleaning_summary.csv` — summary of the cleaning results.
- `requirements.txt` — Python dependency.

## Run
1. Install Python.
2. Run `pip install -r requirements.txt`.
3. Keep all files in the same folder.
4. Run `python clean_dates.py`.

## Method
The script tries explicitly defined date formats rather than guessing. Valid dates are standardized to `YYYY-MM-DD`. The original date column is preserved for traceability. Missing, impossible, or unrecognized dates remain blank in `Clean_Date` and are recorded for verification.

For this sample, slash-separated dates are interpreted as `DD/MM/YYYY`. Confirm the date convention with the data owner before applying this method to real data.

## Results
- Total records: 10
- Valid parsed dates: 7
- Missing or invalid dates: 3

Problem records:
- `O1005`: `31/02/2026` — invalid calendar date.
- `O1006`: blank — missing date.
- `O1009`: `not available` — unrecognized value.

The issue log also records valid dates whose formats were standardized.

## Key learning
Inconsistent dates can affect sorting, filtering, comparisons, and time-based analysis. Explicit parsing, preserving original values, and documenting issues make cleaning transparent and reproducible.

## Interview questions
**Why are dates often problematic?** Different regional formats, missing values, impossible dates, and text entries can prevent reliable analysis.

**What is a date datatype?** A datatype that represents dates (and sometimes times) for chronological sorting, filtering, and date calculations.

## Conclusion
This project demonstrates a basic date-cleaning workflow using Pandas. Uncertain values are documented for verification instead of being guessed.
