

Here are 30 concise SQL interview questions and answers suitable for a Data Engineer role:

***

1. **What is SQL?**  
SQL (Structured Query Language) is used to manage and query relational databases.

2. **Difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN?**  
INNER JOIN returns matching rows; LEFT JOIN returns all from left and matching from right; RIGHT JOIN is opposite; FULL OUTER JOIN returns all rows with matches where they exist.[5]

3. **How to find duplicate rows?**  
Use GROUP BY and HAVING COUNT(*) > 1.

4. **Get the second highest salary from employee table.**  
`SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);`

5. **Difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?**  
RANK() skips numbers after ties, DENSE_RANK() doesn't, ROW_NUMBER() always increases by 1.

6. **What are window functions?**  
SQL functions that perform calculations across a set of rows related to the current row.

7. **What is a CTE (Common Table Expression)?**  
A temporary named result set defined within a query using WITH.

8. **Difference between WHERE and HAVING?**  
WHERE filters rows before grouping; HAVING filters groups after aggregation.

9. **What is normalization?**  
Organizing data to reduce redundancy.

10. **What is denormalization?**  
Introducing redundancy for performance improvements.

11. **What does SELECT DISTINCT do?**  
Returns only unique values of a column.

12. **How do you create an index?**  
`CREATE INDEX idx_name ON table(column);` Improves lookup speed.

13. **What is a primary key?**  
A unique identifier for each row in a table which cannot be NULL.

14. **Difference between primary key and unique key?**  
Both enforce uniqueness; primary key allows only one per table, unique key can be many and allows NULLs.

15. **What are foreign keys?**  
Constraints to ensure referential integrity between tables.

16. **What is a subquery?**  
A query nested inside another query.

17. **Correlated vs. non-correlated subquery?**  
Correlated references columns from outer query; non-correlated does not.

18. **How to get counts by group?**  
`SELECT col, COUNT(*) FROM table GROUP BY col;`

19. **How to remove duplicates?**  
Use SELECT DISTINCT or window function with ROW_NUMBER() and DELETE.

20. **How do you get NULL values?**  
`IS NULL` and `IS NOT NULL` in WHERE clause.

21. **Difference between DELETE and TRUNCATE?**  
DELETE removes rows with conditions and is transactional; TRUNCATE removes all rows, faster, not transactional.

22. **What is UNION vs UNION ALL?**  
UNION removes duplicates, UNION ALL keeps them.

23. **Pattern matching operator in SQL?**  
LIKE with % or _ wildcards.

24. **What are set operators?**  
UNION, UNION ALL, INTERSECT, MINUS/EXCEPT.

25. **What is a view?**  
A saved query (virtual table).

26. **How to update data?**  
`UPDATE table SET col = value WHERE condition;`

27. **How to add a new column to a table?**  
`ALTER TABLE table ADD column datatype;`

28. **How to delete a table?**  
`DROP TABLE table_name;`

29. **How to optimize slow SQL query?**  
Create proper indexes, rewrite joins, filter early, analyze query plan.

30. **What is ACID property?**  
Atomicity, Consistency, Isolation, Durability – properties of reliable transactions.

***

Let me know if you want short query/code examples or deeper explanations for any question!

[1](https://www.datacamp.com/blog/top-sql-interview-questions-and-answers-for-beginners-and-intermediate-practitioners)
[2](https://www.interviewbit.com/sql-interview-questions/)
[3](https://www.youtube.com/watch?v=izlf02YaQ_4)
[4](https://360digitmg.com/blog/data-engineer-sql-interview-questions)
[5](https://www.linkedin.com/posts/christopher-garzon-647081101_20-sql-interview-questions-for-data-engineers-activity-7322970317293772800-1luY)
[6](https://www.geeksforgeeks.org/data-engineering/data-engineer-interview-questions/)
[7](https://www.dataexpert.io/questions)
[8](https://datalemur.com/blog/amazon-sql-interview-questions)
[9](https://www.netcomlearning.com/blog/sql-interview-questions-and-expert-answers)
