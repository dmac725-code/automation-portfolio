"""
Weekly Sales Report Generator
=============================
Reads raw sales data from a CSV file, calculates key metrics,
and generates a formatted summary report.

Usage:
    python generate_weekly_report.py --input sales_data.csv --output report.txt

Requirements:
    pip install pandas
"""

import pandas as pd
import argparse
from datetime import datetime


def load_sales_data(filepath):
    """
    Load and validate the sales CSV file.
    Expected columns: Date, Rep, Client, Product, Amount, Status
    """
    df = pd.read_csv(filepath)

    # Validate required columns exist
    required_cols = ["Date", "Rep", "Client", "Product", "Amount", "Status"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Parse dates and clean amount field
    df["Date"] = pd.to_datetime(df["Date"])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)

    return df


def calculate_metrics(df):
    """
    Calculate key sales metrics from the data.
    Returns a dictionary of metric name -> value.
    """
    metrics = {}

    # Overall totals
    metrics["total_revenue"] = df[df["Status"] == "Closed"]["Amount"].sum()
    metrics["total_pipeline"] = df[df["Status"] == "Pending"]["Amount"].sum()
    metrics["total_lost"] = df[df["Status"] == "Lost"]["Amount"].sum()
    metrics["total_deals"] = len(df)
    metrics["closed_deals"] = len(df[df["Status"] == "Closed"])
    metrics["win_rate"] = (
        metrics["closed_deals"] / metrics["total_deals"] * 100
        if metrics["total_deals"] > 0
        else 0
    )
    metrics["avg_deal_size"] = (
        metrics["total_revenue"] / metrics["closed_deals"]
        if metrics["closed_deals"] > 0
        else 0
    )

    # Per-rep breakdown
    rep_summary = (
        df[df["Status"] == "Closed"]
        .groupby("Rep")["Amount"]
        .agg(["sum", "count"])
        .rename(columns={"sum": "Revenue", "count": "Deals"})
        .sort_values("Revenue", ascending=False)
    )
    metrics["rep_summary"] = rep_summary

    # Top product
    product_revenue = (
        df[df["Status"] == "Closed"].groupby("Product")["Amount"].sum().sort_values(ascending=False)
    )
    metrics["top_product"] = product_revenue.index[0] if len(product_revenue) > 0 else "N/A"
    metrics["top_product_revenue"] = product_revenue.iloc[0] if len(product_revenue) > 0 else 0

    return metrics


def generate_report(metrics, output_path):
    """
    Format metrics into a readable text report and save to file.
    """
    report_date = datetime.now().strftime("%B %d, %Y")

    lines = []
    lines.append("=" * 60)
    lines.append(f"  WEEKLY SALES REPORT — {report_date}")
    lines.append("=" * 60)
    lines.append("")

    # Summary section
    lines.append("SUMMARY")
    lines.append("-" * 40)
    lines.append(f"  Total Revenue (Closed):  ${metrics['total_revenue']:,.2f}")
    lines.append(f"  Pipeline (Pending):      ${metrics['total_pipeline']:,.2f}")
    lines.append(f"  Lost:                    ${metrics['total_lost']:,.2f}")
    lines.append(f"  Total Deals:             {metrics['total_deals']}")
    lines.append(f"  Closed Deals:            {metrics['closed_deals']}")
    lines.append(f"  Win Rate:                {metrics['win_rate']:.1f}%")
    lines.append(f"  Avg Deal Size:           ${metrics['avg_deal_size']:,.2f}")
    lines.append("")

    # Rep breakdown
    lines.append("REP PERFORMANCE")
    lines.append("-" * 40)
    lines.append(f"  {'Rep':<20} {'Revenue':>12} {'Deals':>8}")
    lines.append(f"  {'-'*20} {'-'*12} {'-'*8}")
    for rep, row in metrics["rep_summary"].iterrows():
        lines.append(f"  {rep:<20} ${row['Revenue']:>11,.2f} {int(row['Deals']):>8}")
    lines.append("")

    # Top product
    lines.append("TOP PRODUCT")
    lines.append("-" * 40)
    lines.append(f"  {metrics['top_product']}: ${metrics['top_product_revenue']:,.2f}")
    lines.append("")
    lines.append("=" * 60)
    lines.append("  Report generated automatically.")
    lines.append("=" * 60)

    report_text = "\n".join(lines)

    # Save to file
    with open(output_path, "w") as f:
        f.write(report_text)

    return report_text


def main():
    parser = argparse.ArgumentParser(description="Generate a weekly sales report from CSV data.")
    parser.add_argument("--input", required=True, help="Path to sales data CSV")
    parser.add_argument("--output", default="weekly_report.txt", help="Output report file path")
    args = parser.parse_args()

    # Load, process, generate
    print(f"Loading data from {args.input}...")
    df = load_sales_data(args.input)

    print("Calculating metrics...")
    metrics = calculate_metrics(df)

    print(f"Generating report to {args.output}...")
    report = generate_report(metrics, args.output)

    print("\n" + report)
    print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()
