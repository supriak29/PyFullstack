create database Countries_Cities;

create table country(
id int,
country_name varchar(128),
primary key(id)
);

create table city(
id int,
city_name varchar(128),
postal_code varchar(16) unique ,
country_id int,
primary key (id),
foreign key (country_id) references country(id)
);

######################################################################

select * from countries_cities.country;
select * from countries_cities.city;


######################################################################
######## INSERT INTO country table ########

insert into country values
(1,"Afghanistan"), (2,"Albania"), (3,"Algeria"), (4,"Andorra"), (5,"Angola"), (6,"Antigua and Barbuda"), (7,"Argentina"), (8,"Armenia"), 
(9,"Australia"), (10,"Austria"), (11,"Azerbaijan"), (12,"Bahamas"), (13,"Bahrain"), (14,"Bangladesh"), (15 ,"Barbados"), (16,"Belarus"), 
(17,"Belgium"), (18	,"Belize"), (19	,"Benin"), (20,"Bhutan"), (21,"Bolivia"), (22,"Bosnia and Herzegovina"),(23,"Botswana"),(24,"Brazil"),
(25,"Brunei"),(26,"Bulgaria"),(27,"Burkina Faso"),(28,"Burundi"), (29,"Côte d'Ivoire"),(30,"Cabo Verde"),(31,"Cambodia"), (32,"Cameroon"), 
(33,"Canada"),(34,"Central African Republic"),(35,"Chad"),(36,"Chile"),(37,"China"),(38,"Colombia"),(39,"Comoros"),
(40,"Congo (Congo-Brazzaville)"),(41,"Costa Rica"),(42,"Croatia"),(43,"Cuba"),(44,"Cyprus"),(45,"Czechia (Czech Republic)"),
(46,"Democratic Republic of the Congo"),(47,"Denmark"),(48,"Djibouti"),(49,"Dominica"),(50,"Dominican Republic"),
(51,"Ecuador"),(52,"Egypt"),(53,"El Salvador"),(54,"Equatorial Guinea"),(55,"Eritrea"),(56,"Estonia"),(57,"Eswatini (fmr. 'Swaziland')"),
(58,"Ethiopia"),(59,"Fiji"),(60,"Finland");

####################################################

insert into city values
(1,"Kabul",1001,1), (2,"Kandahar",3801,1), (3, "Herat", 3001,1),
(4,"Tirana",1028,2), (5,"Durrës.",2000 ,2), (6,"Vlorë",9402,2);
