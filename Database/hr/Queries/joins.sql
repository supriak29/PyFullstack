# Process of linking tables is called joining
# SQL provides many kinds of joins: 	1. INNER join
#										2. LEFT join
#                                       3. RIGHT join
#                                       4. FULL OUTER join
#                                       etc.
									


########################################################################################

select first_name, last_name, employees.department_id, departments.department_name 
from employees inner join departments
on departments.department_id = employees.department_id
where employees.department_id in (1,2,3);

###################################################

# Join 3 tables employees, departments & jobs to get the first_name, last_name, job_title & department_id of employees who work in 
# department 1,2,3.

select first_name, last_name, jobs.job_title, departments.department_id
from employees inner join jobs inner join departments
on departments.department_id = employees.department_id and jobs.job_id = employees.job_id
where employees.department_id in (1,2,3);

select first_name, last_name, jobs.job_title, departments.department_id
from employees inner join departments inner join jobs
on departments.department_id = employees.department_id and jobs.job_id = employees.job_id
where employees.department_id in (1,2,3);

######################################################################################