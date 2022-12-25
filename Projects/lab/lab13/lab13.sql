.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where  color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = "blue" and pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having smallest > 0 and count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b
    where a.time < b.time and a.pet = b.pet and a.song = b.song;


CREATE TABLE sevens AS
  SELECT seven from students, numbers
    where students.time = numbers.time and number = 7 and numbers."7" = "True";


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) as lowest_price from inventory group by item;

create table  shoppinglisthelper as
    select name, min(MSRP/rating) from products group by category;

CREATE TABLE shopping_list AS
    select name, store from  shoppinglisthelper, lowest_prices where name = item;

CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs) from shopping_list, stores where shopping_list.store =  stores.store;

