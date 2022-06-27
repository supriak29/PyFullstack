# Trial
select count(*) from actor;
########################################################################################


# 1a. Display the first and last names of all actors from the table actor.
select first_name, last_name from actor;

select actor_id from actor order by actor_id desc;
select max(actor_id) from actor;





# 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select lower(concat(first_name," ",last_name)) as "Actor" from actor;
select upper(concat(first_name," ",last_name)) as "Actor" from actor;

#######################################################################################

# 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, “Joe.”  What is one query would you use to obtain this information?
select actor_id, first_name, last_name from actor where first_name = "Joe";

# 2b. Find all actors whose last name contain the letters GEN:
select first_name, last_name from actor where last_name like "%gen%";

# 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select first_name, last_name from actor where last_name like "%li%" order by last_name, first_name;

# 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country from country where country in ("Afghanistan", "Bangladesh", "China") order by country_id;

###############################################################################

# 3a. Add a middle_name column to the table actor. Position it between first_name and last_name.
select * from actor;
alter table actor add middle_name varchar(15) after first_name; 

# 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
alter table actor modify middle_name blob;
alter table actor modify column middle_name blob;

# 3c. Now delete the middle_name column.
alter table actor drop column middle_name;

#######################################################################################

# 4a. List the last names of actors, as well as how many actors have that last name.
select last_name from actor;
select count(last_name) from actor;

# 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select last_name, count(last_name) as "Count" from actor group by last_name having count(last_name) >= 2;

# 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo’s second cousin’s husband’s yoga teacher. Write a query to fix the record.
select first_name, last_name from actor where first_name = "GROUCHO";
update actor set first_name = "Harpo" where first_name = "GROUCHO" and last_name = "WIILIAMS";
select first_name, last_name from actor order by first_name;

# 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. 
# It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, 
# change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, 
# as that is exactly what the actor will be with the grievous error. 
# BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER!

select actor_id, first_name from actor where first_name = "harpo";

####################################################################################################

# 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
create table address(
address_id int not null,
address varchar(50) not null,
address2 varchar(50),
district varchar(20) not null,
city_id int not null,
postal_code varchar(10),
phone varchar(20) not null,
last_update timestamp not null,
primary key (address_id),
foreign key (city_id) references city(city_id)
);

#############################################################################

# 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:

select first_name, last_name from staff;

select first_name, last_name, address.address 
from staff left join address 
on staff.address_id = address.address_id;


# 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
-- left join: staff.staff_id = payment.staff_id
-- DATE: "2005-08"
-- group by first_name(staff)
-- display: staff name(staff), total amount(payment)
select payment_id, amount, payment_date from payment;
select first_name from staff;
select payment_date from payment where payment_date like "2005-08%";
#-----------------------------------------------------------
select first_name, last_name, sum(payment.amount) as "Total Amount", payment.payment_date
from staff left join payment
on staff.staff_id = payment.staff_id
where payment.payment_date like "2005-08%"
group by first_name, last_name;


# 6c. List each film and the number of actors who are listed for that film. 
# 	  Use tables film_actor and film. Use inner join.
-- left join film_actor.film_id = film.film_id

select title from film; # listing each film
select count(actor_id) from film_actor; # No. of actors
select count(title) from film; # No. of films
#---------------------------------------------------------
select film.film_id, title, count(film_actor.actor_id) as "No. of Actors"
from film left join film_actor
on film.film_id = film_actor.film_id
group by title;


# 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select film_id, title from film where title = "Hunchback Impossible";
select film_id, inventory_id from inventory where film_id = 439;
select count(film_id) from inventory where film_id = 439;
# ------------------------------------------------------------------
# tables: film & inventory
# left join 
# inventory, film
select count(film.title) as "No. of Copies of 'Hunchback Impossible'"
from film left join inventory 
on inventory.film_id = film.film_id
where film.title = "Hunchback Impossible"; 

# 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer.
# List the customers alphabetically by last name:
select customer_id, concat(first_name, "  ",last_name) as "Customer Name" from customer;
select count(customer_id) from customer;
select sum(amount) from payment;	# total payment
-- left join: customer id 
-- tables: customer & payment

select customer.customer_id, customer.first_name, customer.last_name as "Customer Names", sum(payment.amount) as "Total Paid"
from customer left join payment
on customer.customer_id = payment.customer_id
group by customer_id
order by customer.last_name asc;

########################################################################################

# 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
# As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
# Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select title from film where title like 'K%' or title like 'Q%'; # film - table
select language_id, name from language;
select language_id, name from language where name = "english"; # language - table
# --------------------------------------------
select title as "English film" from film where title like 'K%' or title like 'Q%' and language_id = 1 group by title;
# --------------------------------------------------------
select title from film 
where title like 'K%' or title like 'Q%' 
and (select language_id from language where name = "english");


# 7b. Use subqueries to display all actors who appear in the film Alone Trip.
select film_id, title from film where title = "Alone Trip";
select actor_id, film_id from film_actor where film_id = 17;
select actor_id as "Actor ID", concat(first_name,"  ", last_name) as "Actor Names" from actor;

select first_name, last_name from actor where (select title from film where title = "Alone Trip");


# 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.


# 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.


# 7e. Display the most frequently rented movies in descending order.


# 7f. Write a query to display how much business, in dollars, each store brought in.

