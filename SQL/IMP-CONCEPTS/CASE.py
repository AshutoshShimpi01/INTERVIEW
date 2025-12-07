

Here are 10 SQL CASE statement questions with answers—organized as easy, intermediate, and hard:

***

## Easy

1. **What is a SQL CASE statement?**  
A conditional expression that allows you to return different values based on specified conditions, similar to IF-THEN-ELSE.[1][3][4]

2. **Write a query using CASE to label sales above 100 as 'High' and others as 'Low'.**  
```sql
SELECT sale_id, amount,
  CASE WHEN amount > 100 THEN 'High' ELSE 'Low' END AS sale_type
FROM sales;
```

3. **Use CASE to show 'Adult' if age ≥ 18, else 'Minor'.**  
```sql
SELECT name, age,
  CASE WHEN age >= 18 THEN 'Adult' ELSE 'Minor' END AS age_group
FROM users;
```

4. **Use CASE in ORDER BY so records with status 'Active' come first.**  
```sql
SELECT * FROM members
ORDER BY CASE WHEN status = 'Active' THEN 0 ELSE 1 END;
```

## Intermediate

5. **How would you assign grades (A, B, C, F) to students using CASE and score?**  
```sql
SELECT name, score,
  CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 80 THEN 'B'
    WHEN score >= 70 THEN 'C'
    ELSE 'F'
  END AS grade
FROM students;
```

6. **Use multiple CASE statements in the same SELECT for two columns.**  
```sql
SELECT employee_id,
  CASE WHEN age < 30 THEN 'Junior' ELSE 'Senior' END AS seniority,
  CASE WHEN salary > 50000 THEN 'High' ELSE 'Low' END AS salary_range
FROM employees;
```

7. **How do you use CASE in a WHERE clause?**  
You can’t directly use CASE as a condition in WHERE, but you can use it for computed columns, then filter. Example:  
```sql
SELECT * FROM orders
WHERE (CASE WHEN status = 'pending' THEN 1 ELSE 0 END) = 1;
```

8. **Write a query to replace NULL department with 'Unknown' using CASE.**  
```sql
SELECT name,
  CASE WHEN department IS NULL THEN 'Unknown' ELSE department END AS dept
FROM employees;
```

## Hard

9. **Write a query using nested CASE for custom billing:**
```sql
SELECT client, amount,
  CASE
    WHEN amount > 1000 THEN
      CASE WHEN country = 'USA' THEN 'US High' ELSE 'Other High' END
    WHEN amount > 500 THEN 'Medium'
    ELSE 'Low'
  END AS bill_category
FROM bills;
```
(Nested CASE lets you add more detailed logic)[5]

10. **How do you use CASE in an aggregate function?**  
```sql
SELECT
  COUNT(CASE WHEN status = 'Active' THEN 1 END) AS active_count,
  COUNT(CASE WHEN status = 'Inactive' THEN 1 END) AS inactive_count
FROM users;
```
(Counts users by status with CASE inside aggregation)[8]

***

Let me know if you want more examples, explanations, or real-world scenarios!

[1](https://www.w3schools.com/sql/sql_case.asp)
[2](https://mode.com/sql-tutorial/sql-case/)
[3](https://www.programiz.com/sql/case)
[4](https://www.geeksforgeeks.org/sql/sql-case-statement/)
[5](https://trainings.internshala.com/blog/cse-statement-in-sql/)
[6](https://www.w3schools.com/mysql/mysql_case.asp)
[7](https://www.freecodecamp.org/news/case-statement-in-sql-example-query/)
[8](https://www.datacamp.com/tutorial/case-statement-sql)
[9](https://datalemur.com/sql-tutorial/sql-case-statement)
[10](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/case-transact-sql?view=sql-server-ver17)
