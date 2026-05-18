-- Write your query below
SELECT s.seller_name
FROM seller s LEFT JOIN orders o ON o.seller_id = s.seller_id
AND sale_date >= '2020-01-01' AND sale_date <= '2020-12-31'
WHERE o.customer_id IS NULL
ORDER BY s.seller_name ASC