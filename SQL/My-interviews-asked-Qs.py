
select name from employees where dept_id in (select dept_id from departments where location = 'New York');

we know this query works but now we wanna improve the performancs so write a Query : -

using EXISTS : -
select name from employees e where  EXISTS      -- correlated subquery
(select 1 from departments d where e.dept_id = d.dept_id and location = 'New York');

------------------------------------

INFOY

-- second highest salary from emp table

select max(salary) from employees where salary not in (select max(salary) from employees);

with ch as
(select name,salary,
rank() over(order by salary desc) as rk
from employees e)
select *
from ch
where rk = 2;     -- here 3rd, 4th, 5th any number of highest 


------------------------------------

ONIX


-- find all employees whose salary is greater than the average salary of all employees in the table

select * from employees where salary > (select avg(salary) as av from employees);



------------------------------------

ZS


-- Top 3 customers by total spending in year 2024 for each region.
(cust_name,region,total_spnt)

Top 3 customers by total spending in year 2024;

with total as
(select c.cust_name,c.region,sum(o.total_amount) as total_spnt
from Customers c
join Orders o on c.cust_id = o.cust_id
where order_date between '2024-01-01' and '2024-12-31'
group by c.cust_name,c.region),
rr as
(
select cust_name, region, total_spnt,
rank() over(partition by region order by total_spnt desc) as rk
from total
)
select *
from rr
where rk< 4;


------------------------------------
DROP DUPLICATES


WITH DuplicateCTE AS 
(
    SELECT ID, 
      ROW_NUMBER() OVER(PARTITION BY Name ORDER BY ID ASC) as rn
    FROM YourTable
)
DELETE FROM
    YourTable
WHERE ID IN (SELECT ID FROM DuplicateCTE WHERE rn > 1);


------------------------------------
UPDATE COLUMN

update Orders
set customer_id = 
CASE
WHEN customer_id = 4 THEN 3
WHEN customer_id = 3 THEN 4
ELSE customer_id END;


------------------------------------

IMPT

SELECT
    SUM(CASE WHEN Value > 0 THEN Value ELSE 0 END) AS Pos_Sum,
    SUM(CASE WHEN Value < 0 THEN Value ELSE 0 END) AS Neg_Sum
FROM
    FinancialTransactions;


------------------------------------







------------------------------------


