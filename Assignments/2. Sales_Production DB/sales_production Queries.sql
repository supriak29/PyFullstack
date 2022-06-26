# ASSIGNMENT 2: 
# SALES AND PRODUCTION TABLE
# Use the Sales and Production database for the following assignment.
################################################################################################

# Q1) Find the first name and last name of all customers:
select first_name, last_name from customers;


# Q2) Find the first names, last names, and emails of all customers:
select first_name, last_name , email from customers;


#Q3) To get data from all customers columns
select * from customers;


# Q4) Find the customers located in California.
# select city, state from customers order by state;  # California - CA
select first_name, last_name, state from customers where state = "CA";


#Q5) Sort the customers by their first names in ascending order.
select first_name from customers order by first_name asc;


 
# Q6) Return all the cities of customers located in California and the number of customers in each city.
#	select city from customers where state = "CA" order by city;
select city, count(city) from customers group by city having count(city) > 1;



#Q7) Return the city in California which has more than ten customers:
#	select city, state from customers where state = 'CA';
#	select count(city) from customers group by city having count(city) > 1;
#	select city, count(city) from customers group by city having (select count(city) from customers where state = "CA") > 10
#	select count(customer_id) as "Total customers" from customers;
	select customer_id, first_name, last_name, city, state from customers where state = "CA" order by city;

select customer_id, concat(first_name,"  ",last_name) as "Customers",city, state, count(city) as "More than 10 customers" 
from customers group by city having count(city) > 10 and state = "CA";




#Q8) Sort the customer list by the first name in ascending order:
select * from customers order by first_name asc;



#Q9) Sort the customer list by the first name in descending order.
select * from customers order by first_name desc;



#Q10) Sort the city, first_name, last_name by city and first_name
#select city, first_name, last_name from customers order by city desc;
select city, first_name, last_name from customers order by city, first_name;
