create database companies_plans;

create table company(
id int,
company_name varchar(255),
VAT_ID varchar(16) unique,
email varchar(255),
city_id int,
company_address varchar(255),
details text,
is_active bool,
primary key (id),
foreign key (city_id) references Countries_Cities.city(id)
);

create table user_account(
id int,
first_name varchar(128),
last_name varchar(128),
email varchar(255),
user_name varchar(255),
password varchar(255),
is_active bool,
ts_created timestamp not null default current_timestamp,
ts_updated timestamp not null default current_timestamp,
company_id int,
primary key(id),
foreign key(company_id) references companies_plans.company(id)
);

create table invoice_company(
id int,
company_id int,
invoice_amount decimal(10,2),
invoice_period varchar(255),
invoide_details text,
ts_issued timestamp default current_timestamp,
ts_paid timestamp not null default current_timestamp,
ts_cancelled timestamp not null default current_timestamp,
primary key(id),
foreign key(company_id) references companies_plans.company(id)
);

create table plan(
id int primary key,
plan_name varchar(64),
details varchar(255),
rooms_min int,
rooms_max int not null,
monthly_price decimal(10.2)
);

create table company_plan(
id int primary key,
company_id int,
plan_id int,
ts_created timestamp default current_timestamp,
ts_activated timestamp default current_timestamp,
ts_deactivated timestamp default current_timestamp,
foreign key(company_id) references company(id),
foreign key(plan_id) references plan(id)
);

create table company_plan_status_catalog(
id int primary key,
status_name varchar(64),
plan_is_active bool
);

create table company_plan_status_events(
id int primary key,
company_plan_id int,
company_plan_status_catalog_id int,
ts timestamp default current_timestamp,
foreign key(company_plan_id) references company_plan(id),
foreign key(company_plan_status_catalog_id) references company_plan_status_catalog(id)
);

#######################################################################

select * from companies_plans.company;
select * from companies_plans.company_plan;
select * from companies_plans.company_plan_status_catalog;
select * from companies_plans.company_plan_status_events;
select * from companies_plans.invoice_company;
select * from companies_plans.plan;
select * from companies_plans.user_account;

#######################################################################


