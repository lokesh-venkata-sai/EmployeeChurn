create database employee;
use employee;

create table users(
id int primary key, 
username varchar(30) not null, 
email varchar(50) not null unique);

create table feedback(
id int primary key,
q1 int,q2 int,q3 int,q4 int,q5 int,q6 int,q7 int,
 q8 int,q9 int,q10 int,q11 int,q12 int,q13 int,q14 int,
 q15 int,q16 int,q17 int,q18 int,q19 int, foreign key(id) references users(id));


 create table churn(
id int primary key,
churn int,
foreign key(id) references feedback(id));
 
insert into users  values(567,'exam','exam@gmail.com');
insert into users  values(456,'exam1','exam1@gmail.com');
insert into users values(111,'username','user@email.com');
insert into users values(102,'exam4','exam4@gmail.com');

insert into feedback  values(567,1,3,5,4,3,2,1,4,1,2,3,4,5,1,3,2,5,3,4);
