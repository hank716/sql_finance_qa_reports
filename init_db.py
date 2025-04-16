
import sqlite3
import os
import random
from datetime import datetime, timedelta

db_path = os.path.join("db", "finance.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS transactions")
cur.execute("DROP TABLE IF EXISTS accounts")

cur.execute("""
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    opened_at DATE
)
""")
cur.execute("""
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    account_id INTEGER,
    amount REAL,
    type TEXT CHECK(type IN ('deposit', 'withdraw')),
    timestamp DATETIME,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
)
""")

names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"]
for i, name in enumerate(names, 1):
    opened = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    cur.execute("INSERT INTO accounts (id, name, opened_at) VALUES (?, ?, ?)", (i, name, opened.date()))
    for _ in range(random.randint(5, 15)):
        t_type = random.choice(["deposit", "withdraw"])
        amount = round(random.uniform(100, 5000), 2)
        t_date = opened + timedelta(days=random.randint(1, 365))
        cur.execute("INSERT INTO transactions (account_id, amount, type, timestamp) VALUES (?, ?, ?, ?)",
                    (i, amount, t_type, t_date.strftime("%Y-%m-%d %H:%M:%S")))

conn.commit()
conn.close()
print("Initialized db/finance.db with sample data.")
