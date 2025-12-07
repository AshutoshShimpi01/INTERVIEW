
select name from employees where dept_id in (select dept_id from departments where location = 'New York');

we know this query works but now we wanna improve the performancs so write a Query : -

using EXISTS : -
select name from employees e where  EXISTS      -- correlated subquery
(select 1 from departments d where e.dept_id = d.dept_id and location = 'New York');




-- second highest salary from emp table
with ch as
(select name,salary,
rank() over(order by salary desc) as rk
from employees e)
select *
from ch
where rk = 2;     -- here 3rd, 4th, 5th any number of highest 


-- find all employees whose salary is greater than the average salary of all employees in the table

select * from employees where salary > (select avg(salary) as av from employees);
