# ORDER BY

# ORDER BY is an optional clause of select statement
# ORDER BY clause allows you to sort the rows returned by the select clause by one or more sort expressions in ascending or descending order

##############################################

select employee_id, first_name, last_name, hire_date, salary from employees;

select employee_id, first_name, last_name, hire_date, salary from employees order by first_name;

select employee_id, first_name, last_name, hire_date, salary from employees order by salary;

select employee_id, first_name, last_name, hire_date, salary from employees order by hire_date;

select employee_id, first_name, last_name, hire_date, salary from employees order by hire_date desc;