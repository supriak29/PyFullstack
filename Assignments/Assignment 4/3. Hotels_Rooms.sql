create database hotels_rooms;
 
 create table category(
 id int primary key,
 category_name varchar(128)
 );
 
 create table hotel(
 id int primary key,
 hotel_name varchar(128),
 description text,
 company_id int,
 city_id int,
 category_id int,
 is_active bool,
 foreign key(company_id) references companies_plans.company(id),
 foreign key(city_id) references countries_cities.city(id),
 foreign key(category_id) references hotels_rooms.category(id)
 );
 
 create table room_type(
 id int primary key,
 type_name varchar(128)
 );
 
 create table room(
 id int primary key,
 room_name varchar(128),
 description text,
 hotel_id int,
 room_type_id int,
 current_price decimal(10,2),
 foreign key(hotel_id) references hotels_rooms.hotel(id),
 foreign key(room_type_id) references hotels_rooms.room_type(id)
 );
 
 ############################################################################3
 
 select * from hotels_rooms.category;
 select * from hotels_rooms.guest;
 select * from hotels_rooms.hotel;
 select * from hotels_rooms.room;
 select * from hotels_rooms.room_type;
 