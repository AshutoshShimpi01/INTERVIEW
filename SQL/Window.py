

Here are 10 SQL window function questions with answers—organized by easy, intermediate, and hard:

***

## Easy

1. **What is a window function in SQL?**  
A function that performs calculations across a set of rows related to the current row, using the `OVER()` clause.[3][4][5]

2. **How do you use ROW_NUMBER()?**  
Assigns a unique number to each row based on ordering.  
```sql
SELECT emp_name, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank FROM employees;
```

3. **How do you calculate running totals with SUM()?**  
```sql
SELECT month, sales,
  SUM(sales) OVER (ORDER BY month) AS running_total
FROM sales_data;
```

4. **Give an example of PARTITION BY in window functions.**  
```sql
SELECT department, emp_name, salary,
  AVG(salary) OVER (PARTITION BY department) AS avg_dept_salary
FROM employees;
```

## Intermediate

5. **How do you rank items within groups using RANK()?**  
```sql
SELECT department, emp_name, salary,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

6. **What does LAG() do in window functions?**  
Fetches a value from a previous row.  
```sql
SELECT emp_name, salary,
  LAG(salary) OVER (ORDER BY hire_date) AS prev_salary
FROM employees;
```

7. **How do you count over a window with COUNT()?**  
```sql
SELECT order_id, COUNT(*) OVER (PARTITION BY customer_id) AS customer_order_count
FROM orders;
```

## Hard

8. **How can you use LEAD() for comparing future values?**  
Retrieves a value from a following row.  
```sql
SELECT date, sales,
  LEAD(sales) OVER (ORDER BY date) AS next_day_sales
FROM sales_data;
```

9. **Show how to use ROWS BETWEEN for moving averages.**  
```sql
SELECT date, sales,
  AVG(sales) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM sales_data;
```

10. **How do you use FIRST_VALUE() to get the first sale of each customer?**  
```sql
SELECT customer_id, sale_date, amount,
  FIRST_VALUE(sale_date) OVER (PARTITION BY customer_id ORDER BY sale_date) AS first_sale_date
FROM sales;
```

***

Let me know if you need more advanced analytic examples or deeper explanations!

[1](https://www.coginiti.co/tutorials/intermediate/sql-window-functions/)
[2](https://mode.com/sql-tutorial/sql-window-functions/)
[3](https://www.geeksforgeeks.org/sql/window-functions-in-sql/)
[4](https://www.sqltutorial.org/sql-window-functions/)
[5](https://www.freecodecamp.org/news/window-functions-in-sql/)
[6](https://www.stratascratch.com/blog/the-ultimate-guide-to-sql-window-functions/)
[7](https://datalemur.com/sql-tutorial/sql-aggregate-window-functions)
[8](https://www.youtube.com/watch?v=S1do1EeA7ng)
[9](https://learnsql.com/blog/sql-window-functions-examples/)
