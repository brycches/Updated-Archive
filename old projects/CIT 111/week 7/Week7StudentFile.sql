USE v_art;
-- Use the art database

-- Show me the first three pieces of artwork in alphabetical order
SELECT title
FROM artwork

-- Show me all the different periods from the artwork (only one of each)

-- Show me the artwork from the artist with id #3

-- Show me artwork with the title's that start with A to I

-- Show me the title of the artwork for the years 1800 to 1900

-- Show me the artwork titles for the periods 'Modern' and 'Baroque'

-- Show me the titles and periods for the artwork that has the period having part of the word 'impr'

-- Show me the titles and periods for the artwork that has the period having part of the word 'impr'
-- Use REGEXP now

-- Show me the title and period of the artwork that begins with word Post

-- Show me the title and period of the artwork that ends with 'ism'

-- Show me the title of the artwork that begins with the word 'Old'

-- Show me the title and period of the artwork that has 'the' 'in' or 'on' in the title
-- Show me the title and period of the artwork that begins with word Post
SELECT title, period
FROM artwork
WHERE period REGEXP '^post';
-- ^ caret(^) matches Beginning of string

-- Show me the title and period of the artwork that ends with 'ism'
SELECT title, period
FROM artwork
WHERE period REGEXP 'ism$';
-- $ End of string

-- Show me the title of the artwork that begins with the word 'Old'
SELECT title 
FROM artwork
WHERE title REGEXP '^Old';

-- Show me the title and period of the artwork that has 'the' 'in' or 'on' in the title
SELECT title
FROM artwork
WHERE title REGEXP 'the|in|on';
-- notice Mona Lisa has 'on' in it

-- Show me the title and period of the artwork that has the words 'the' 'in' or 'on' in the title
SELECT title
FROM artwork
WHERE title REGEXP ' the | in | on ';

-- Show me the full name of an artist for those who have middle names and sort it by an Alias called Middle

USE bike;
-- From the bike database
-- Show me products, model years, and list price but display list price as the column 'Price' 
-- without editing the database and from the most expensive to least expensive
 SELECT * FROM product;
 
 SELECT product_name, model_year, list_price AS Price
 FROM product
 ORDER by Price DESC;
 
 
-- Show me products, model years, and list price 
-- but round it and display the column as 'Rounded Price' without editing the database
 SELECT product_name, model_year, ROUND(list_price, 0) AS "Rounded Price"
 FROM product;
 
-- Show it but with the list price too as a column
  SELECT product_name, model_year, list_price, ROUND(list_price, 0) AS "Rounded Price"
 FROM product;
 
-- Show me the products, model years, and list price and add $100 to each without editing the database 
SELECT product_name, model_year, list_price + 100
 FROM product;
 
-- Show me products, model years, and list price and list the column as "price_adjustment"
 SELECT product_name, model_year, list_price + 100 AS price_adjustment
 FROM product;
 
-- Show me products, model years, and list price and list the column as "price_adjustment" 
-- and show me only the prices over $1000
 SELECT product_name, model_year, list_price + 100 AS price_adjustment
 FROM product
 WHERE list_price + 100 > 1000;
 
-- Show me the products and model year of the products that start with Trek or Surly
-- (but not from 2016)
SELECT product_name, model_year
FROM product
WHERE (product_name LIKE 'Trek%' OR product_name LIKE 'Surly%') AND NOT model_year = 2016;

SELECT product_name, model_year
FROM product
WHERE (product_name REGEXP '^Trek' OR product_name REGEXP '^Surly') AND model_year <> 2016;