
SELECT account_id
FROM transactions
GROUP BY account_id, date(timestamp)
HAVING COUNT(*) >= 5
UNION
SELECT account_id
FROM transactions
WHERE amount > 10000;
