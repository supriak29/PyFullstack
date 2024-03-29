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

# gives records of those which have deparment_id as 8, 9 only.
select employee_id, first_name, last_name, department_id from employees where department_id in (8,9) order by department_id;

# gives records of those which have deparment_id as 8, 9, 10 only.
select employee_id, first_name, last_name, department_id from employees where department_id in (8,9,10) order by department_id;

# below query will result same: 
select employee_id, first_name, last_name from employees where first_name in ("Lex","Jack","John");
select employee_id, first_name, last_name from employees where first_name = "Lex" or first_name="Jack" or first_name="John" or last_name="Grant";

######### LIKE
# This operator compares a value to similar value using wild card operator.
# SQL provides 2 wild cards:
# 1. %  (percentage sign): represents zero, one or multiple character
# 2. _ (underscore): represents a single character

# first name starting with first 2 characters as "jo"
select employee_id, first_name, last_name from employees where first_name like 'jo%' order by first_name;

# first name that ends with last two characters as "en"
select employee_id, first_name, last_name from employees where first_name like '%en' order by first_name;

# first name that has it's 2nd character as 'h' as only 1 underscore is used
select employee_id, first_name, last_name from employees where first_name like '_h%' order by first_name;

# first name that has it's 4th character as 'a' as 3 underscore is used
select employee_id, first_name, last_name from employees where first_name like '___a%' order by first_name;

######### ALL
# This operator compares a value to all values in another value set

select first_name, last_name, salary 
from employees 
where salary >= ALL (select salary from employees where department_id = 8)
order by salary desc;


######### ANY
# This operator compares a value to any value in a set according to the condition.

# (normal query)
select department_id, first_name, last_name, salary 
from employees
order by department_id;

# 1. grouping all the employees under department_id: 1, 2, 3, ... seperately
# 2. getting average salary of employees under avg(dept 1), avg(dept 2), avg(dept 3),... seperately
# 3. eg. avg salary for dept 2 = (13000 + 6000) = 9500
# 4. select any of the record under dept 2 having salary > avg salary of that particular dept
# 5. eg. 13000 > 9500 and 6000 < 9500;  therefore we only display record having salary 13000 from dept 2.

select department_id, first_name, last_name, salary 
from employees 
where salary > any (select avg(salary) from employees group by department_id) 
order by first_name, last_name;


select department_id, first_name, last_name, salary 
from employees 
where salary > any (select avg(salary) from employees group by department_id) 
order by department_id;


select department_id,first_name, last_name, department_id, avg(salary) as "Average Salary" 
from employees 
group by department_id;

# Query split 1
select department_id,first_name, last_name, avg(salary) from employees group by department_id;

# Query split 2
select first_name, last_name, salary, department_id
from employees where department_id = 2;


######### EXISTS
# This checks if a sub-query contains any rows
# if sub-query returns one or more rows, the result of the exist is true, otherwise the result is false.
# this query finds all employees who have dependents

# below query displays the records from employees which also come under dependent table
select employee_id, first_name, last_name from employees e where exists(select * from dependents d where d.employee_id = e.employee_id);
select employee_id, first_name, last_name from employees;
select * from dependents order by employee_id;

######### NOT
# to negate the result of any boolean expression, you use NOT operator
select department_id, first_name, last_name, salary from employees where department_id = 5 and not salary > 5000 order by salary; 
select employee_id, salary from employees where salary > 5000;

######### NOT IN 
# to negate the IN operator
select employee_id, first_name, last_name, department_id from employees where department_id not in (1,2,3) order by department_id;

######### NOT LIKE
# to negate LIKE operator
select first_name, last_name from employees where first_name not like "D%" order by first_name;

######### NOT BETWEEN
# to negate the effect of BETWEEN
select employee_id, first_name, last_name, salary from employees where salary not between 3000 and 5000 order by salary;