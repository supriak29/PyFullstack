create database guests;

create table guest(
id int primary key,
first_name varchar(128),
last_name varchar(128),
email varchar(255),
phone varchar(255) not null,
address varchar(255) not null,
details text not null
);

create table invoice_guest(
id int primary key,
guest_id int,
reservation_id int,
invoice_amount decimal(10,2),
ts_issued timestamp default current_timestamp,
ts_paid timestamp not null default current_timestamp,
ts_cancelled timestamp not null default current_timestamp,
foreign key(guest_id) references guests.guest(id),
foreign key(reservation_id) references reservations.reservation(id)
);

########################################################################

select * from guests.guest;
select * from guests.invoice_guest;