# LOGICAL OPERATORS

######### AND  
select employee_id, first_name, last_name, salary from employees where salary > 5000 and salary < 7000 order by salary;

######### OR
select employee_id, first_name, last_name, salary from employees where salary = 5000 OR salary = 7000 order by salary;
select employee_id, first_name, last_name, salary from employees where salary = 8000 OR salary = 7000 order by salary;

######### BETWEEN
# This operator searches for value that are within a set of values, given the min & max values.
# These values also include the min & max values.
select employee_id, first_name, last_name, salary from employees where salary between 9000 and 10000 order by salary;

######### IN
# This operator compares a value to a list of specified values
select employee_id, first_name, last_name, department_id from employees where department_id in (8,9) order by department_id;
select employee_id, first_name, last_name, department_id from employees where department_id in (8,9,10) order by department_id;

######### LIKE
# This operator compares a value to similar value using wild card operator.
# SQL provides 2 wild cards:
# 1. % ---- (percentage sign) represents zero, one or multiple character
# 2. _ ---- (underscore) represents a single character
select employee_id, first_name, last_name from employees where first_name like 'jo%' order by first_name;
select employee_id, first_name, last_name from employees where first_name like '%en' order by first_name;
select employee_id, first_name, last_name from employees where first_name like '_h%' order by first_name;
select employee_id, first_name, last_name from employees where first_name like '___a%' order by first_name;

######### ALL
# This operator compares a value to all values in another value set

select first_name, last_name, salary 
from employees 
where salary >= ALL (select salary from employees where department_id = 8)
order by salary desc;


######### ANY
# This operator compares a value to any value in a set according to the condition.

select first_name, last_name, salary 
from employees 
where salary > any (select avg(salary) from employees group by department_id) 
order by first_name, last_name;

select first_name, last_name, department_id, avg(salary) as "Average Salary" 
from employees 
group by department_id;

# Query split 1
select first_name, last_name, avg(salary) from employees;

# Query split 2
select first_name, last_name, salary, department_id
from employees where department_id = 1;
