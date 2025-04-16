
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    opened_at DATE
);
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    account_id INTEGER,
    amount REAL,
    type TEXT CHECK(type IN ('deposit', 'withdraw')),
    timestamp DATETIME,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);
