revenew
profit

how many customer are to board in flight
create table customer(cust_id int NOT NULL AUTO_INCREMENT,cust_name varchar(25),f_id int,foreign key(f_id) references flight(f_id),PRIMARY KEY(cust_id));
Query OK, 0 rows affected (0.021 sec)
create table ticket(t_id int NOT NULL AUTO_INCREMENT,f_id int,foreign key(f_id) references flight(f_id),cust_id int,foreign key(cust_id) references customer(cust_id),d_date DATE,status varchar(25),PRIMARY KEY(t_id));
Query OK, 0 rows affected (0.022 sec)
create table seats(s_id int PRIMARY KEY,f_id int,foreign key(f_id) references flight(f_id),price int,available_seat int);
Query OK, 0 rows affected (0.023 sec)

details abt customers, flight no: -> customer details
select f.f_id,f.a_name,c.cust_id,c.cust_name from customer c,flight f where f.f_id=c.f_id and f.f_id=1;
+------+-------------+---------+-----------+
| f_id | a_name      | cust_id | cust_name |
+------+-------------+---------+-----------+
|    1 | King_fisher |      12 | vidya     |
|    1 | King_fisher |      13 | vicky     |
|    1 | King_fisher |      14 | stefan    |
+------+-------------+---------+-----------+
check how many flights are scheduled this week
 select a_id,from_loc,to_loc from flight where d_time BETWEEN '2022-09-12 12:00:00' AND '2022-09-18 12:00:00';
+------+-----------+-----------+
| a_id | from_loc  | to_loc    |
+------+-----------+-----------+
|  101 | bangalore | pune      |
|  102 | chennai   | bangalore |
|  103 | chennai   | pune      |
+------+-----------+-----------+
how much money received from per flight
 select SUM(s.price),s.f_id from seats s GROUP BY s.f_id;
+--------------+------+
| SUM(s.price) | f_id |
+--------------+------+
|         1200 |  101 |
|         1000 |  102 |
|         1000 |  103 |
+--------------+------+




admin
login
flight details
Customer
Ticket booking

create database airline;
use airline;
create table admin(a_id int  NOT NULL AUTO_INCREMENT, a_name varchar(25),PRIMARY KEY(a_id));
create table flight(f_id int NOT NULL AUTO_INCREMENT, a_id int,a_name varchar(25), from_loc varchar(25), to_loc varchar(25), d_time DATETIME,a_time DATETIME,duration int,total_seats int,PRIMARY KEY(f_id));
create table customer(cust_id int NOT NULL AUTO_INCREMENT,cust_name varchar(25),f_id int,foreign key(f_id) references flight(f_id),PRIMARY KEY(cust_id));

create table ticket(t_id int NOT NULL AUTO_INCREMENT,f_id int,foreign key(f_id) references flight(f_id),cust_id int,foreign key(cust_id) references customer(cust_id),d_time DATETIME,foreign key(d_time) references flight(d_time),status varchar(25),PRIMARY KEY(t_id));
create table seats(s_id int PRIMARY KEY,foreign key(f_id) references flight(f_id),foreign key(d_time) references flight(d_time),price int,available_seat int);
