alter table user modify date_of_birth varchar(10);
alter table user modify date_of_birth date;
alter table user modify mobile varchar(10);
alter table user modify username varchar(15);

select * from user;




delete from user where email="kush@gmail.com";

ALTER TABLE user ADD pwdkey varchar(255) after date_of_birth; 
ALTER TABLE user ADD fernet varchar(255) after pwdkey; 
ALTER TABLE user ADD hash varchar(255) after date_of_birth; 

alter table user drop fernet;
alter table user drop pwdkey;
alter table user drop hash;

select * from user where email="kush@gmail.com";