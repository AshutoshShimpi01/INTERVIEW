



Here are 10 SQL CTE (Common Table Expression) questions with answers, grouped by easy, intermediate, and hard:

***

## Easy

1. **What is a CTE in SQL?**  
A Common Table Expression is a temporary, named result set defined using `WITH` and referenced within the same query, improving readability and modularity.[1][3][6]

2. **Basic CTE syntax example:**  
```sql
WITH HighEarners AS (
  SELECT name, salary FROM employees WHERE salary > 50000
)
SELECT * FROM HighEarners;
```

3. **Can you reference a CTE in multiple places in a query?**  
Yes; you can join, filter, or aggregate the CTE as you would with a table.

4. **What is the benefit of a CTE over a subquery?**  
CTEs make queries easier to read, debug, and allow referencing results multiple times in a statement.[2][5]

## Intermediate

5. **How do you use multiple CTEs in one query?**  
Comma-separate each CTE after `WITH`, then reference by name.  
```sql
WITH DeptCount AS (SELECT department_id, COUNT(*) AS cnt FROM employees GROUP BY department_id),
     AvgSalary AS (SELECT department_id, AVG(salary) AS avg_sal FROM employees GROUP BY department_id)
SELECT * FROM DeptCount JOIN AvgSalary USING(department_id);
```

6. **How do you use a CTE for aggregation?**  
Use a CTE to calculate aggregates, then select or join results.  
```sql
WITH DeptAvg AS (
  SELECT department_id, AVG(salary) AS avg_sal FROM employees GROUP BY department_id
)
SELECT * FROM DeptAvg WHERE avg_sal > 60000;
```

7. **Can you INSERT, UPDATE, or DELETE using a CTE?**  
Yes; for example,  
```sql
WITH ToUpdate AS (
  SELECT id FROM products WHERE price < 10
)
UPDATE products SET price = 10 WHERE id IN (SELECT id FROM ToUpdate);
```

## Hard

8. **What is a recursive CTE and give an example?**  
A CTE that references itself to process hierarchical/recursive data.  
```sql
WITH RECURSIVE counter AS (
  SELECT 1 AS n
  UNION ALL
  SELECT n + 1 FROM counter WHERE n < 5
)
SELECT n FROM counter;
```

9. **How would you use a recursive CTE for a tree/hierarchy structure (e.g., managers)?**  
```sql
WITH Managers AS (
  SELECT id, name, manager_id FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id
    FROM employees e JOIN Managers m ON e.manager_id = m.id
)
SELECT * FROM Managers;
```

10. **Can you use a CTE in a CREATE VIEW statement?**  
Yes.  
```sql
CREATE VIEW TopEmployees AS
WITH TopEmp AS (SELECT * FROM employees WHERE salary > 90000)
SELECT * FROM TopEmp;
```

***

Let me know if you want more complex recursive examples or use cases for CTEs!

[1](https://www.datacamp.com/tutorial/cte-sql)
[2](https://learnsql.com/blog/cte-with-examples/)
[3](https://www.geeksforgeeks.org/sql/cte-in-sql/)
[4](https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql?view=sql-server-ver17)
[5](https://www.atlassian.com/data/sql/using-common-table-expressions)
[6](https://www.tutorialspoint.com/sql/sql-common-table-expression.htm)
[7](https://hightouch.com/sql-dictionary/sql-common-table-expression-cte)
[8](https://docs.snowflake.com/en/user-guide/queries-cte)
[9](https://www.youtube.com/watch?v=K1WeoKxLZ5o)
[10](https://stackoverflow.com/questions/4740748/when-to-use-common-table-expression-cte)
