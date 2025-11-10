

Here are 10 SQL subquery questions with answers, organized as easy, intermediate, and hard:

***

## Easy

1. **What is a subquery in SQL?**  
A subquery is a query nested inside another SQL statement (SELECT, INSERT, UPDATE, or DELETE) to use its result.[2][3][5]

2. **Write an example to find employees with a salary above the company's average using a subquery.**  
```sql
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

3. **Find orders for customers in 'Ahmednagar' using a subquery.**  
```sql
SELECT * FROM orders
WHERE customer_id IN (SELECT id FROM customers WHERE city = 'Ahmednagar');
```

## Intermediate

4. **Update employees whose department is in New York (use subquery in UPDATE).**  
```sql
UPDATE employees
SET bonus = 1000
WHERE department_id IN (SELECT department_id FROM departments WHERE city = 'New York');
```

5. **Delete products not present in any orders (subquery in DELETE).**  
```sql
DELETE FROM products
WHERE id NOT IN (SELECT product_id FROM order_items);
```

6. **Select employees whose salary matches the maximum FOR each department (correlated subquery).**  
```sql
SELECT name, department_id, salary
FROM employees e
WHERE salary = (
  SELECT MAX(salary) FROM employees WHERE department_id = e.department_id
);
```

## Hard

7. **Select departments that have more than 5 employees (subquery with GROUP BY and HAVING).**  
```sql
SELECT department_id FROM departments
WHERE department_id IN (
  SELECT department_id FROM employees GROUP BY department_id HAVING COUNT(*) > 5
);
```

8. **Find customers who never placed any orders (subquery with NOT EXISTS).**  
```sql
SELECT name FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

9. **Subquery in FROM clause: Get average salary per department using a subquery as a derived table.**  
```sql
SELECT department_id, avg_salary
FROM (SELECT department_id, AVG(salary) AS avg_salary FROM employees GROUP BY department_id) avg_dept;
```

10. **Nested subquery: Find products with a price equal to the lowest price where category is ‘Books’.**  
```sql
SELECT name, price
FROM products
WHERE price = (
  SELECT MIN(price) FROM products WHERE category = 'Books'
);
```

***

Let me know if you want more practice, explanations, or other advanced subquery types!

[1](https://www.datacamp.com/tutorial/sql-subquery)
[2](https://www.scaler.com/topics/sql/types-of-subqueries-in-sql/)
[3](https://www.geeksforgeeks.org/sql-server/sql-server-subquery/)
[4](https://www.dbvis.com/thetable/the-complete-guide-to-sql-subqueries/)
[5](https://data-flair.training/blogs/sql-subquery/)
[6](https://www.geeksforgeeks.org/sql/sql-subquery/)
[7](https://www.almabetter.com/bytes/tutorials/sql/types-of-subqueries-in-sql)
[8](https://mode.com/sql-tutorial/sql-sub-queries/)
[9](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17)
[10](https://www.youtube.com/watch?v=JksrTuEVEPk)
