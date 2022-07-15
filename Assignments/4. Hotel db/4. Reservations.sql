create database reservations;

create table reservation(
id int primary key,
guest_id int,
start_date date,
end_date date,
ts_created timestamp default current_timestamp,
ts_updated timestamp default current_timestamp,
discount_percent decimal(5,2),
total_price decimal(10,2),
foreign key(guest_id) references guests.guest(id)
);

create table room_reserved(
id int primary key,
reservation_id int,
room_id int,
price decimal(10,2),
foreign key(reservation_id) references reservations.reservation(id),
foreign key(room_id) references hotels_rooms.room(id)
);

create table reservation_status_catalog(
id int primary key,
status_name int 
);

create table reservation_status_events(
id int primary key,
reservation_id int,
reservation_status_catalog_id int,
details text not null,
ts_created timestamp default current_timestamp,
foreign key(reservation_id) references reservations.reservation(id),
foreign key(reservation_status_catalog_id) references reservations.reservation_status_catalog(id)
);

create table channel(
id int primary key,
channel_name varchar(255),
details text
);

create table channel_used(
room_id int,
channel_id int,
primary key(room_id, channel_id),
foreign key(room_id) references hotels_rooms.room(id),
foreign key(channel_id) references reservations.channel(id)
);

create table syncronization(
id int primary key,
reservation_id int,
channel_id int,
message_sent text,
message_received text not null,
ts timestamp default current_timestamp,
foreign key(reservation_id) references reservations.reservation(id)
);

###########################################################################3

select * from reservations.channel;
select * from reservations.channel_used;
select * from reservations.reservation;
select * from reservations.reservation_status_catalog;
select * from reservations.reservation_status_events;
select * from reservations.room_reserved;
select * from reservations.syncronization;


