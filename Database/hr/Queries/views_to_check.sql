# VIEWS

# Virtual Tables
# does not increase memory
# creating a new table (eg. region_country)
# originally we have 7 tables in hr database. these tables are main tables needed for long period of time.
# when we create another table, then we will have 8 tables in all. this 8th table will have real existence which thereby will increase the db. 
# also this new table might be needed for small period of time
# to avoid that, we create views. even after execution, the 8th table will remain with us. 

# STEPS to create views:
#	1. rigth click on Views
#	2. create view...

#	3.	creating view:  
##			CREATE VIEW `new_view_name` AS
##			< paste the query that you want to perform >

# 	4. save the view -> apply -> apply -> finish

#	4. to drop a view: 
##			drop view.


###########################################################################

## RUNNING THE VIEWS as below: 

select * from region_country;
select country_name, region_name from region_country;
