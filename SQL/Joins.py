


Here are 10 SQL JOIN questions with answers, ranging from easy to hard:

***

## Easy

1. **What is an INNER JOIN?**  
Returns rows with matching values in both tables.  
_Eg:_  
```sql
SELECT a.id, b.name FROM tableA a INNER JOIN tableB b ON a.id = b.id;
```

2. **What is a LEFT JOIN?**  
Returns all rows from the left table and matched rows from the right; unmatched rows show NULLs on the right.  
_Eg:_  
```sql
SELECT a.id, b.name FROM tableA a LEFT JOIN tableB b ON a.id = b.id;
```

3. **What is a RIGHT JOIN?**  
Returns all rows from the right table and matched rows from the left; unmatched rows show NULLs on the left.  
_Eg:_  
```sql
SELECT a.id, b.name FROM tableA a RIGHT JOIN tableB b ON a.id = b.id;
```

4. **What is a FULL OUTER JOIN?**  
Returns all rows from both tables; unmatched rows show NULLs from either side.  
_Eg:_  
```sql
SELECT a.id, b.name FROM tableA a FULL OUTER JOIN tableB b ON a.id = b.id;
```

5. **What is a CROSS JOIN?**  
Returns all possible combinations of rows from the two tables (Cartesian product).  
_Eg:_  
```sql
SELECT a.id, b.name FROM tableA a CROSS JOIN tableB b;
```

***

## Intermediate

6. **Write a query to find employees without a department using LEFT JOIN.**  
```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
```

7. **What is a SELF JOIN? Give an example.**  
A table joined to itself, used for hierarchical or relational data.  
_Eg:_  
```sql
SELECT a.name AS Employee, b.name AS Manager
FROM employees a
INNER JOIN employees b ON a.manager_id = b.id;
```

8. **How do you join three tables with INNER JOIN?**  
```sql
SELECT a.id, b.name, c.amount
FROM orders a
INNER JOIN customers b ON a.customer_id = b.id
INNER JOIN payments c ON a.payment_id = c.id;
```

***

## Hard

9. **Find all customers who placed no orders using LEFT JOIN.**  
```sql
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.customer_id IS NULL;
```

10. **Explain what happens if join key values are NULL.**  
Joins ignore rows where the join key is NULL; such rows won’t match and will appear as unmatched rows (showing NULLs) in OUTER JOINs.

***

Let me know if you want code practice or deeper explanations for any join type!

[1](https://www.w3schools.com/sql/sql_join.asp)
[2](https://www.geeksforgeeks.org/sql/sql-join-set-1-inner-left-right-and-full-joins/)
[3](https://www.dbvis.com/thetable/sql-cheat-sheet-every-join-explained/)
[4](https://datalemur.com/sql-tutorial/sql-joins-inner-outer-left-right)
[5](https://www.scholarhat.com/tutorial/sqlserver/different-types-of-sql-joins)
[6](https://www.programiz.com/sql/join)
[7](https://www.atlassian.com/data/sql/sql-join-types-explained-visually)
[8](https://www.youtube.com/watch?v=0OQJDd3QqQM)
[9](https://www.datacamp.com/cheat-sheet/sql-joins-cheat-sheet)
