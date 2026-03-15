# Automation Demo: Weekly Sales Report Generator

## The Problem
Client's sales team was manually building weekly reports in Excel every Friday — copying data, calculating totals, formatting tables. Took 1-2 hours each week.

## What I Delivered
A Python script that:
1. Reads raw sales data from a CSV file
2. Calculates key metrics (revenue, pipeline, win rate, avg deal size)
3. Breaks down performance by sales rep
4. Identifies top-selling product
5. Generates a formatted text report
6. Runs with a single command: `python generate_weekly_report.py --input data.csv`

## Files Included
- `generate_weekly_report.py` — The automation script (fully commented)
- `sample_sales_data.csv` — Sample input data for testing
- `sample_report_output.txt` — What the generated report looks like

## Key Features
- **Input validation** — Checks for required columns, handles missing data gracefully
- **Clean formatting** — Currency formatting, aligned columns, clear sections
- **Flexible** — Works with any CSV that has the expected columns
- **Documented** — Every function has comments explaining what it does
- **Zero manual steps** — One command, full report

## Time Saved
- Before: 1-2 hours/week manually
- After: Under 10 seconds, automated
- Annual savings: ~75 hours

## Turnaround
Script built and tested in under 4 hours.
