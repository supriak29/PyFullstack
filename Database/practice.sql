-- **	Sakila	***

-- 1a. Display the first and last names of all actors from the table actor.
select first_name, last_name from actor;
-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select upper(concat(first_name," ",last_name)) as "Actor Name" from actor;
# lower case 
select lower(concat(first_name," ",last_name)) as "Actor Name" from actor;


-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, “Joe.” What is one query would you use to obtain this information?
# option 1 (preferred):
select actor_id, first_name, last_name from actor where first_name="Joe";
# option 2:
select actor_id, first_name, last_name from actor where first_name in ("Joe");

-- 2b. Find all actors whose last name contain the letters GEN:
select first_name, last_name from actor where last_name like ("%GEN%");

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select first_name, last_name from actor where last_name like ("%LI%") order by last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
# option 1 (preferred): 
select country_id, country from country where country in ("Afghanistan", "Bangladesh", "China");
# option 2:
select country_id, country from country where country="Afghanistan" or country="Bangladesh" or country="China";

-- ------------------------------------------------------------------
# ALTER:	
#		1. adding a column
#		2. ('after' keyword): adding a column at specified position
#		3. ('modify' keyword): changing the datatype of a column
#		4. ('drop' keyword): deleting a column
-- ------------------------------------------------------------------

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name.
#	STEPS: 
# 		1. we need to alter table: actor
#		2. add the column middle_name along with it's datatype & length
#		3. this col is added after first_name (thereby, before last_name) ---> then it will be in between first_name & last_name
alter table actor add middle_name varchar(45) after first_name;
select * from actor;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
#   STEPS:
#		1. alter the table: actor
#		2. modify it's datatype: from varchar to blob
alter table actor modify middle_name blob;


-- 3c. Now delete the middle_name column.
#	STEPS:
#		1. alter the table: actor
#		2. delete/drop the required col: middle_name
alter table actor drop middle_name;


-- 4a. List the last names of actors, as well as how many actors have that last name.
select last_name from actor;
select last_name, count(last_name) as "count" from actor group by last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
# option 1 (preferred):
select last_name, count(last_name) as "count" from actor group by last_name having count(last_name) >= 2;
# option 2:
select last_name, count(last_name) as "count" from actor where (select count(last_name) from actor) >= 2 group by last_name;

-- -------------------------------
# UPDATE:
#		used when a particular record needs to be updated/changed inside the table
# 		update uses "SET" keyword to set the new value
#	STEPS:
#		1. update: actor
# 		2. set the value <column_name="value">
# 		3. provide condition if any
-- -------------------------------

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo’s second cousin’s husband’s yoga teacher. Write a query to fix the record.
select first_name, last_name from actor where first_name="GROUCHO";
update actor set first_name="HARPO" where first_name="GROUCHO" and last_name="WILLIAMS";
select first_name, last_name from actor where first_name="HARPO";


-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 
-- In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. 
-- Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. 
-- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER!

# 1. for the above, we will also need the respective actor_id for adding condition
# 2. since we are dealing with changing the value, we use UPDATE 
# 3. CASE is used
##		case
##		when <condition>
##		then <"value to be stored in first_name">
##		else
##		<other solution>
## 		end
#	4. where clause along with condition

select actor_id, first_name, last_name from actor where first_name="HARPO";

update actor set first_name =
case
when first_name="HARPO"
then "GROUCHO"
else "MUCHO GROUCHO"
end
where actor_id=172;



-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
create table address;


-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
# checking who all are the staffs: 
select first_name, last_name from staff;
# we can either use LEFT Join or INNER join
# using Left join: as it will give address for all those mentioned on left side:
# meaning: from staff s left join address a --------- all from staff & it's respective field from address
select s.first_name, s.last_name, a.address
from staff s left join address a
on a.address_id = s.address_id;

select s.first_name, s.last_name, a.address
from staff s inner join address a
on a.address_id = s.address_id;


-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
# since staff_id is common in both tables: staff & payment,
# and staff_id is PK in staff table ----- FK in payment table
# we write: s.staff_id = p.staff_id

-- left join: staff.staff_id = payment.staff_id
-- DATE (yyyy-mm-dd) should begin with: "2005-08"---> therefore, we use like (%) --> "2005-08%" (meaning, where date begins with 2005-08)
-- group by first_name(staff)
-- display: staff name(staff), total amount(payment)

select s.staff_id,s.first_name, s.last_name from staff s;
select p.staff_id, p.amount,p.payment_date from payment p;

select s.first_name, s.last_name, sum(p.amount) as "Total amount", p.payment_date
from staff s left join payment p
on s.staff_id = p.staff_id
where p.payment_date like "2005-08%"
group by s.first_name;


-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select film_id, title from film;
select film_id, actor_id from film_actor;

select f.title, count(fa.actor_id) as "No. of actors listed"
from film f inner join film_actor fa
on f.film_id = fa.film_id
group by f.title;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select * from inventory;
select count(film_id) from inventory where film_id=439;

select film_id,title from film where title="Hunchback Impossible";

select title, count(i.inventory_id) as "Copies in inventory"
from film f inner join inventory i
on f.film_id = i.film_id
where title="Hunchback Impossible"
group by title;

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
select c.customer_id ,c.first_name, c.last_name from customer c;
select p.customer_id, p.amount from payment p;

select c.customer_id, c.first_name, c.last_name, sum(p.amount) as "Total amount paid"
from customer c left join payment p
on c.customer_id = p.customer_id
group by p.customer_id
order by last_name; 

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select language_id, title from film where title like 'K%' or title like 'Q%';
select language_id, name from language where name="English";

# option 1: 
select title from film 
where title like 'K%' or title like 'Q%'
and (select language_id from language where name="English") ;

# option 2:
select title from film 
where language_id in  (select language_id from language where name="English") 
and title like 'K%' or title like 'Q%';


-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
select actor_id, first_name, last_name from actor;
select film_id, title from film where title="Alone Trip";
select actor_id, film_id from film_actor where film_id=17;

select first_name, last_name from actor
where actor_id in (select actor_id from film_actor where film_id = (select film_id from film where title="Alone Trip"));



-- 7c. You want to run an email marketing campaign in Canada, 
-- for which you will need the names and email addresses of all Canadian customers. 
-- Use joins to retrieve this information.
#	country(country_id, country)
#	city(city_id, city; country_id)
#	address(address_id; city_id)
#	customer(customer_id; address_id, first_name, last_name, email)
select * from customer;
select * from country where country="canada";

# using SUB-QUERY
select first_name, last_name, email 
from customer where address_id in 
(select address_id from address where city_id in 
(select city_id from city where country_id in 
(select country_id from country where country="Canada")
));

# using JOIN
select first_name, last_name, email
from customer 
left join address on address.address_id = customer.address_id 
left join city on city.city_id = address.city_id
left join country on country.country_id = city.country_id
where country = "Canada"; 

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as family films.
#	film(film_id, title)
#	film_category(film_id, category_id)
#	category(category_id, name)
select film_id, category_id from film_category where category_id=8;
select category_id, name from category where name="family";
select film_id, title from film;

# JOIN
select film.film_id, film.title from film
left join film_category on film.film_id = film_category.film_id
left join category on category.category_id = film_category.category_id
where category.name="family";

# SUB-QUERY
select film_id, title from film
where film_id in (select film_id from film_category 
where category_id= (select category_id from category where name = "family"));

-- 7e. Display the most frequently rented movies in descending order.
#	rental(customer_id, inventory_id)
# 	inventory(inventory_id, film_id)
#	film(film_id, title)
select inventory_id, customer_id from rental order by inventory_id;
select inventory_id, count(customer_id) from rental group by inventory_id;
select inventory_id, count(inventory_id) from rental group by inventory_id;
select inventory_id, film_id from inventory;
select film_id, count(inventory_id) from inventory group by film_id;
select film_id, title from film;

# JOIN

select inventory.film_id, film_text.title, count(rental.inventory_id) from inventory
inner join rental on inventory.inventory_id = rental.inventory_id
inner join film_text on inventory.film_id = film_text.film_id
group by rental.inventory_id
order by count(inventory.inventory_id) desc;


-- 7f. Write a query to display how much business, in dollars, each store brought in.

select * from payment;

select store.store_id, sum(payment.amount) from store
inner join staff on store.store_id = staff.store_id
inner join payment on staff.staff_id = payment.staff_id
group by store.store_id;

