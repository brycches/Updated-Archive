-- Use the bike DB
USE bike;
-- Add some text with two columns like this: "The 'store_name' email is 'email'" 


-- if we used store_id which is an integer that would become a part of the string and would not be an integer any more.

-- Show me only the first 10 characters for all the product names


-- Show me only the last 10 characters for all the product names

-- Show me the number count of letters including spaces for the product names

-- Trim the spaces from a line of text

-- Trim the right side

-- Trim the left side

-- Change all the text to upper case for store names

-- Change all the text to lower case for store names

-- parameters for LOCATE(find, search, [start]) returns an integer of where it is located
-- Show me the starting location letter's number of the word 'Girl' and return the product name too 
-- only display the ones that have the word Girl

-- parameters for SUBSTRING(string, start, length)--

-- Show me the text from product_names starting at character 9 and show the next 6 characters

-- Show me only the word "Girl's" in product_names
SELECT SUBSTRING(product_name, LOCATE('Girl', product_name), 4), product_name
FROM product
WHERE product_name LIKE '%girl%';

-- Use the art database
USE v_art;

-- Art database return the starting location of the word 'woman' for all artwork 
-- (and returning 0 if it doesn't have the word)
SELECT LOCATE('woman', title), title
FROM artwork;

-- Do the same thing but return the word 'Woman' (5 letters long)
SELECT SUBSTRING(title, LOCATE('woman', title), 5), title
FROM artwork
WHERE LOCATE('woman', title);

-- NUMERIC functions

-- Use the bike DB
USE bike;
-- Round the list price from products and show the price - do it for 1 digit, 2 digits, 3, no parameter
SELECT ROUND(list_price, 0), list_price
FROM product;

-- Roundup  the list price from products and show the price
SELECT CEILING(2.01);
SELECT FLOOR(2.01);
SELECT ROUND(2.01);




-- Return the prices with the dollar sign in front
SELECT CONCAT('$', FORMAT(list_price, 2)), list_price
FROM product;

-- DATE functions


-- Show me the year of the order date
SELECT YEAR(order_date), order_date
FROM cust_order;


-- Show me the day of the order date
SELECT DAY(order_day), order_date
FROM cust_order;

-- Show me the month of the order date
SELECT MONTH(order_day), order_date
FROM cust_order;

-- Show me the minute of now
SELECT MINUTE(now());
SELECT NOW();
SELECT SYSDATE();
-- Show me the second in time of now
SELECT SECOND(SYSDATE());
-- Show me the system date and time
SELECT SYSDATE();
-- Show me how many days until Halloween
SELECT DATEDIFF('2024-10-31', NOW()) AS 'Days until Halloween';

-- Show me how long it took to ship from the order date
-- days it took from order to shipped

SELECT DATEDIFF(shipped_date, order_date) AS daystoship, shipped_date, order_date
FROM cust_order;

-- Add 9 days to the orderdate 


-- What does this do? 
SELECT CEILING(DATEDIFF('2023-12-25', '2023-6-25') / 7 );

-- Format Code	Description
-- %c	Month, numeric
-- %M	Month name
-- %e	Day of the month, numeric
-- %D	Day of the month with suffix
-- %y	Year, 2 digits
-- %Y	Year, 4 digits
-- %W	Weekday name





