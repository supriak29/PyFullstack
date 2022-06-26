# select select_list from table_name
# First, specify a list of comma-sepparated columns from the table in the select clause.
# Then, specify the table name in the FORM clause.
# If you execute two SQL select statements, you need to separate them using the semicolon (;).

select * from employees;

# SQL SELECT - selecting data from specific columns
# To select data from specific columns, you can specify the column list after the select clause of the select statement.

select employee_id, first_name, last_name, hire_date from employees;

# SQL SELECT - performing a simple calculation
# The following example uses the select statement to get the first name, last name, salary and new salary.

select first_name, last_name, salary, salary * 1.05 from employees;

# To assign an expression or a column an alias, you specify the AS keyword followed by the column alias as follows.

select first_name, last_name, salary, salary * 1.05 as new_salary from employees;

