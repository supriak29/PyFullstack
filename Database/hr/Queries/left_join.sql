# LEFT JOIN

# Returns all the rows from left table whether or not there is a matching rows in the right table
# Each location belongs to one and only one country while each country can have zero or more locations.

#######################################################################
select country_id, country_name 
from countries
where country_id in ('UK','US','CN');

select country_id, street_address, city 
from locations
where country_id in ('UK','US','CN');

select c.country_name, c.country_id, l.country_id, l.street_address, l.city
from countries c left join locations l
on l.country_id = c.country_id
where c.country_id in ('UK','US','CN');

#################

# Location, Region, Country - 3 tables left join

select * from regions;
select region_id from regions;
select region_id from countries;


select r.region_name,c.country_name, l.street_address, l.city
from countries c 
left join locations l on l.country_id = c.country_id
left join regions r on r.region_id = c.region_id
where c.country_id in ('UK','US','CN');
