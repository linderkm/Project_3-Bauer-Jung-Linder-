ALTER TABLE player RENAME COLUMN "Server" TO server;
ALTER TABLE character RENAME COLUMN "Age" TO age;

--Query all fields from the table
SELECT * FROM player;

--Query data to return all rows containing age range under 18
SELECT age
FROM player
WHERE age = 'Under 18';

--Query data to return all rows containing player info for age range under 18
SELECT Gender, Sexuality, Country
FROM player
WHERE age = 'Under 18';

--Query data to return all rows containing age range 18 to 30
SELECT age
FROM player
WHERE age = '18 to 30';

--Query data to return all rows containing player info for age range 18 to 30
SELECT Gender, Sexuality, Country
FROM player
WHERE age = '18 to 30';

--Query data to return all rows containing age range 31 to 42
SELECT age
FROM player
WHERE age = '31 to 42';

--Query data to return all rows containing player info for age range 31 to 42
SELECT Gender, Sexuality, Country
FROM player
WHERE age = '31 to 42';

--Query data to return all rows containing age range 43 to 55
SELECT age
FROM player
WHERE age = '43 to 55';

--Query data to return all rows containing player info for age range 43 to 55
SELECT Gender, Sexuality, Country
FROM player
WHERE age = '43 to 55';

