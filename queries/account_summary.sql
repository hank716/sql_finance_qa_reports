
SELECT 
  a.id AS account_id,
  a.name AS account_name,
  SUM(CASE WHEN t.type = 'deposit' THEN t.amount ELSE 0 END) AS total_deposit,
  SUM(CASE WHEN t.type = 'withdraw' THEN t.amount ELSE 0 END) AS total_withdraw,
  SUM(
    CASE 
      WHEN t.type = 'deposit' THEN t.amount 
      WHEN t.type = 'withdraw' THEN -t.amount 
      ELSE 0 
    END
  ) AS balance
FROM accounts a
LEFT JOIN transactions t ON a.id = t.account_id
GROUP BY a.id;
