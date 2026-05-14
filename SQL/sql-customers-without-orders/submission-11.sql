-- Write your query below
SELECT temp.name FROM 
(SELECT c.name, o.customer_id, COUNT(customer_id) FROM 
customers c LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.name, o.customer_id
HAVING COUNT(customer_id) < 1) as temp
;