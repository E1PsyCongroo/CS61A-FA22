CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child
    FROM parents, dogs WHERE parent = name ORDER BY -height;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size from dogs, sizes where height > min and height <= max;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
    select a.child as first, c.size as first_size, b.child as second, d.size as second_size
    from parents as a, parents as b, size_of_dogs as c, size_of_dogs as d
    where a.parent = b.parent and a.child < b.child and c.name = a.child and d.name = b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
    select "The two siblings, " || a.first || " plus " || a.second || " have the same size: " || a.first_size as sentence
    from siblings as a, siblings as b where a.first = b.first  and a.second = b.second and a.first_size = b.second_size;

