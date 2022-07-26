# STORED PROCEDURE in SQL

# A procedure (often called as stored procedure) is a subroutine like a sub-program in a regular flow.

# STEPS to write our own Stored Procedure: 
# 	1. rigth click on Stored Procedures
#	2. create stored procedures

## 	3. a sample is given as below: 
##		CREATE PROCEDURE `new_procedure_name` ()
##		BEGIN
##				<create your own stored procedure body>
##				<	eg. select * from employees;	>
##		END

#	4. save -> apply -> apply -> finish

##	5. call the required stored procedure ---> SYNTAX: call new_procedure_name;
##										  ---> EG.:    call show_employees; 

#######################################################################

# BUILT-IN stored procedures
select now(); 		# current date & time
select version();
show privileges;
show databases;
show tables;  # will only show the tables only if a database is selected


# USER-DEFINED stored procedures
call show_employees;
call left_join;




