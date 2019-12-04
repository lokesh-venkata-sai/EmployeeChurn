create database employee;
use employee;

create table users(
id int primary key, 
username varchar(30) not null, 
email varchar(50) not null unique,
satisfaction float,
churn int);

create table feedback(
id int primary key,
q1 int,q2 int,q3 int,q4 int,q5 int,q6 int,q7 int,
 q8 int,q9 int,q10 int,q11 int,q12 int,q13 int,q14 int,
 q15 int,q16 int,q17 int,q18 int,q19 int, foreign key(id) references users(id));
 
insert into users  values(567,'exam','exam@gmail.com',null,null);
insert into users  values(456,'exam1','exam1@gmail.com',null,null);
insert into users values(111,'username','user@email.com',null,null);
insert into users values(102,'exam4','exam4@gmail.com',null,null);
insert into users values(103,'exam3','exam3@gmail.com',null,null);
insert into users values(105,'exam5','exam5@gmail.com',null,null);
insert into users values(106,'exam6','exam6@gmail.com',null,null);
insert into users values(107,'exam7','exam7@gmail.com',null,null);
insert into users values(108,'exam8','exam8@gmail.com',null,null);
insert into users values(109,'exam9','exam9@gmail.com',null,null);
insert into users values(110,'exam10','exam10@gmail.com',null,null);


insert into feedback  values(567,1,3,5,4,3,2,1,4,1,2,3,4,5,1,3,2,5,3,4);

create table details(id int,
last_evaluation float,
 number_project int,
       average_montly_hours int, 
       time_spend_company int,
       Work_accident int,
       promotion_last_5years int,
       Departments int, #(1 to 9)
       salary int, #(1 to 3)
       foreign key(id) references users(id)) ;


insert into details values(567,0.4,4,157,3,0,1,2,1);
insert into details values(456,0.4,4,157,3,0,1,2,1);
insert into details values(111,0.47,2,154,3,0,0,7,1);
insert into details values(102,0.4,3,127,5,1,1,8,2);
insert into details values(103,0.7,4,157,3,0,1,3,1);
insert into details values(105,0.8,2,135,3,1,1,5,3);
insert into details values(106,0.4,3,127,5,1,1,9,2);
insert into details values(107,0.7,4,157,3,0,1,2,1);
insert into details values(108,0.8,2,135,3,1,1,4,3);
insert into details values(109,0.4,3,127,5,1,1,8,2);
insert into details values(110,0.7,4,157,3,0,1,3,1);
