
import sqlite3
import pandas as pd
import argparse
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--account", type=str, help="Filter by account name (optional)")
    parser.add_argument("-s", "--start", type=str, help="Start date YYYY-MM-DD")
    parser.add_argument("-e", "--end", type=str, help="End date YYYY-MM-DD")
    parser.add_argument("--csv", action="store_true", help="Output CSV")
    args = parser.parse_args()

    conn = sqlite3.connect("db/finance.db")
    df = pd.read_sql_query("""
        SELECT a.name, t.type, t.amount, t.timestamp
        FROM transactions t
        JOIN accounts a ON a.id = t.account_id
    """, conn)

    if args.account:
        df = df[df["name"].str.contains(args.account, case=False, na=False)]
    if args.start:
        df = df[df["timestamp"] >= args.start]
    if args.end:
        df = df[df["timestamp"] <= args.end]
    df = df.sort_values(by="timestamp")

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    html = template.render(
        accounts_data=[
            {"name": name, "transactions": df_group[["timestamp", "type", "amount"]].to_dict(orient="records")}
            for name, df_group in df.groupby("name")
        ],
        generated_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        account_filter_display=args.account or "All",
        date_range_display=f"{args.start or 'Start'} to {args.end or 'End'}"
    )

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated report.html")

    if args.csv:
        df.to_csv("report.csv", index=False)
        print("Generated report.csv")

if __name__ == "__main__":
    main()
