# SQL Finance QA Reports

SQL Finance QA Reports is a complete project for querying and generating financial transaction reports. It uses Python and SQLite to simulate realistic banking data, with both CLI and Web UI interfaces that allow generating visual HTML reports. This project is suitable for data analysis, SQL practice, testing automation, or financial data prototype development.

---

## 🔧 Project Features

- SQLite database for lightweight and portable storage
- Supports both CLI and Flask-based Web UI query interfaces
- HTML and CSV report export
- Randomly generated mock accounts and transactions to simulate real banking behavior
- Modular project structure designed for easy testing, extension, and deployment
- Can be integrated into ETL, test validation, or dashboard systems

---

## 📁 Project Structure

```
sql_finance_qa_reports/
├── app/                        # Flask web application
│   ├── app.py                  # Flask startup script
│   └── templates/              # HTML form and report templates
├── db/                         # SQLite database
│   └── finance.db
├── data/
│   └── sample_data.sql         # Optional SQL seed data
├── schema/
│   └── banking_schema.sql      # Table schema for accounts and transactions
├── queries/
│   ├── top_transactions.sql
│   ├── suspicious_accounts.sql
│   └── account_summary.sql
├── reports/
│   └── html_report.py          # CLI report generator (optional)
├── templates/
│   └── report_template.html    # Jinja2 template for CLI mode
├── init_db.py                  # Generate mock accounts & transactions
├── generate_report.py          # CLI report generator
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Environment

### Conda Recommended Setup

```bash
conda create -n finance_qa_env python=3.10 -y
conda activate finance_qa_env
pip install -r requirements.txt
```

---

## 🏁 Usage Guide

### 1️⃣ Initialize the database

```bash
python init_db.py
```

- Generates 30 random accounts
- 5–15 transactions per account (deposits/withdrawals)
- Output database file: `db/finance.db`

---

### 2️⃣ CLI Mode: Generate Reports

```bash
python generate_report.py -a Alice -s 2023-01-01 -e 2023-12-31 --csv
```

| Option      | Description                              |
|-------------|------------------------------------------|
| `-a`        | Fuzzy match on account name              |
| `-s`, `-e`  | Start and end date filtering             |
| `--csv`     | Output to CSV in addition to HTML report |

> Outputs:
> - `report.html`: clean formatted report
> - `report.csv`: raw exportable data (optional)

---

### 3️⃣ Web UI Mode (Flask)

```bash
python app/app.py
```

Then open in your browser:
```
http://127.0.0.1:5000/
```

- 🔍 Search account name (fuzzy match)
- 📅 Filter start and end dates
- 📊 Visual HTML report rendered inline

---

## 🔍 Built-in SQL Query Templates (in `queries/`)

- `top_transactions.sql`: Top 5 highest-value transactions
- `suspicious_accounts.sql`: High-frequency or large transactions
- `account_summary.sql`: Deposit, withdrawal, and balance per account

Can be executed manually or as reference for automation.

---

## 📦 Python Dependencies

- `pandas`: for tabular data operations
- `Jinja2`: for HTML templating
- `Flask`: for running the web app
- `sqlite3`: Python standard DB engine

---

## 📌 Use Cases

- SQL test scenario generation
- Mock data for finance dashboards
- Data + Web integration portfolio project
- Lightweight reporting system prototype

---

## 🔒 License

For learning and demo purposes only. This project contains no real user or financial data. Do not use in production environments without proper review.
