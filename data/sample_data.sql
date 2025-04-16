
INSERT INTO accounts (id, name, opened_at) VALUES
(1, 'Alice Smith', '2023-01-01'),
(2, 'Bob Johnson', '2023-02-15');

INSERT INTO transactions (account_id, amount, type, timestamp) VALUES
(1, 1000, 'deposit', '2023-01-01 10:00:00'),
(1, 200, 'withdraw', '2023-01-03 15:00:00'),
(2, 5000, 'deposit', '2023-02-16 09:00:00');
