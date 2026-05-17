-- Write your query below
SELECT DISTINCT
    c.customer_id,
    c.customer_name
FROM customers c
JOIN orders a
    ON c.customer_id = a.customer_id
JOIN orders b
    ON c.customer_id = b.customer_id
WHERE a.product_name = 'A'
  AND b.product_name = 'B'
  AND c.customer_id NOT IN (
      SELECT customer_id
      FROM orders
      WHERE product_name = 'C'
  )
ORDER BY c.customer_name;