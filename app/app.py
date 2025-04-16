from flask import Flask, render_template, request
import sqlite3
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        account = request.form.get("account", "")
        start_date = request.form.get("start_date", "")
        end_date = request.form.get("end_date", "")
        return render_report(account, start_date, end_date)
    return render_template("form.html")

def render_report(account_filter, start, end):
    conn = sqlite3.connect("db/finance.db")
    df = pd.read_sql_query("""
        SELECT a.name, t.type, t.amount, t.timestamp
        FROM transactions t
        JOIN accounts a ON a.id = t.account_id
    """, conn)

    if account_filter:
        df = df[df["name"].str.contains(account_filter, case=False, na=False)]
    if start:
        df = df[df["timestamp"] >= start]
    if end:
        df = df[df["timestamp"] <= end]

    grouped = [
        {"name": name, "transactions": group[["timestamp", "type", "amount"]].to_dict(orient="records")}
        for name, group in df.groupby("name")
    ]

    context = {
        "accounts_data": grouped,
        "generated_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "account_filter_display": account_filter or "All",
        "date_range_display": f"{start or 'Start'} to {end or 'End'}"
    }
    return render_template("report_template.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
