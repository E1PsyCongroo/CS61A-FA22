.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b
    WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;



CREATE TABLE sevens AS
  SELECT s.seven FROM students AS s, numbers AS c WHERE s.number = 7 AND c.'7' = 'True' AND s.time = c.time;


CREATE TABLE average_prices AS
  SELECT category as category, AVG(msrp) as average_price FROM products GROUP BY category;
  -- alternate solution
  -- SELECT category, SUM(msrp)/COUNT(*) FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;
  -- alternate solution
  -- SELECT * FROM inventory GROUP BY item HAVING MIN(price);


CREATE TABLE shopping_list AS
  SELECT name, store FROM products AS p, lowest_prices AS l
    WHERE l.item = p.name
    GROUP BY category HAVING MIN(MSRP/rating);


CREATE TABLE total_bandwidth AS
  SELECT SUM(s.mbs) FROM stores AS s, shopping_list AS sl WHERE s.store = sl.store;

