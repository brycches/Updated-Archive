SELECT @@global.sql_mode;

SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,
NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,
NO_ENGINE_SUBSTITUTION';

-- Let's use the v_art database, select it
USE v_art;

-- Show me the country, firstname, and lastname from the table artist
SELECT country, fname, lname
FROM artist;

-- Show me the artist are from France?
SELECT country, fname, lname
FROM artist
WHERE country = 'france';

-- How many artist are from France? What if there were thousands?
SELECT COUNT(country)
FROM artist
WHERE country = 'france';

-- This next one won't work, why?
-- Can't use fname and lname anymore because the summary count doesn't go with one person
SELECT country, COUNT(country), fname, lname
FROM artist
WHERE country = 'france';

-- But we could use country because that is the same for all
SELECT country, COUNT(country)
FROM artist
WHERE country = 'france';

-- Switch to the bike database
USE bike;

-- Show me the list prices of the products
SELECT list_price
FROM product;

-- Show me the average list price
SELECT AVG(list_price)
FROM product;

-- Show me the average list price with only two decimals, outputs an integer
SELECT ROUND(AVG(list_price),2) AS averagelistprice
FROM product;

-- Outputs with comma and is a string
SELECT FORMAT(AVG(list_price),2) averagelistprice
FROM product;

-- Show me the total cost of all the items
SELECT SUM(list_price)
FROM product;

SELECT list_price FROM product;

-- Show me the most expensive and least expensive item in one query
SELECT MAX(list_price) AS 'most expensive' , MIN(list_price) AS 'least expensive'
FROM product;

-- Show me which one (item) is the most expensive
SELECT product_name, list_price
FROM product
ORDER BY list_price DESC
LIMIT 1;
-- OR 
SELECT product_name, list_price
FROM product
WHERE list_price IN (SELECT MAX(list_price) FROM product);

-- Show me the average list price for 2016 models
-- If I wanted the average of each model year I could get one year at a time this way
SELECT AVG(list_price)
FROM product
WHERE model_year = '2016';

-- Show me the average list price for 2017 models
SELECT AVG(list_price)
FROM product
WHERE model_year = '2017';

-- And I'd have to do that for each year. What if I wanted all the years at once?
-- Show me the average list price of each model year listed by year
SELECT model_year, AVG(list_price)
FROM product
GROUP BY model_year;

-- DOES NOT WORK
SELECT model_year, AVG(list_price)
FROM product
WHERE model_year;

-- filtering before it's grouped
-- Order of execution:
-- FROM WHERE GROUP BY HAVING SELECT ORDER BY LIMIT
-- For with God, He sends out love

-- Show me the average list price of each model year listed by year only if the list prices are over $2800

-- WITH ROLLUP is a subclause of GROUP BY, average of all the averages
-- Show me the average list price of each model year listed by year only if the list prices are over $2800
-- Then show me the final average of all the averages


-- Do the same one but show me the total 
-- Sum of all the sums 'Grand Total' - still for each model year listed by year only if the list prices are over $2800


-- Same as above but only count each price once
-- If we had bikes the same price we might not want to include the same price twice in the average

-- Same as above but instead of DISTINCT try ALL and then without them
-- ALL is the default and is assumed when not there 
-- Delete ALL vs DISTINCT

-- Same as above with ALL but use COUNT instead of AVG - see how it works well with COUNT

-- Same as above with COUNT instead of AVG but use DISTINCT instead of all 
-- Here we can count all the unique list_prices over 2800

-- Remember this one:

-- HAVING filters after the grouping. Remember you only have access to what has been grouped and 
-- aggregated (values and aggregates that are part of the group). 
-- It's right there with SELECT in the Order of Execution
-- FROM WHERE GROUP BY HAVING SELECT ORDER BY LIMIT

-- Show me the average list price of each model year listed by year only if the list prices are over $2800
-- BUT ONLY SHOW me those model years with their averages over $4000
-- This is another IF filter but you have to have the column in the SELECT whereas the WHERE can be any column

-- This doesn't work, why?
-- Be careful using FORMAT in a HAVING clause (it's a string not a number at that point)
USE bike;
SELECT model_year, FORMAT(AVG(list_price),2) AS avgp
FROM product
WHERE list_price;
-- WHERE can use any column in the base table but HAVING can't

-- WHERE can use any column in the base table but HAVING can't

-- An average of each brand
SELECT brand_name, CONCAT('$', FORMAT(AVG(list_price),2)) AS AverageBrandPrice
FROM product p
JOIN brand b
ON p.brand_id = b.brand_id
GROUP BY brand_name WITH ROLLUP;
-- Filtering before and after the grouping


-- Switch to the magazine database
USE magazine;
SELECT * FROM magazine;
SELECT * FROM subscriber;
SELECT * FROM subscription;

-- How many people subscribe to Beautiful Birds
SELECT magazineName, COUNT(*) AS numberOfSubscribers
FROM subscription s
	JOIN magazine m
		ON s.magazineKey = m.magazineKey
WHERE magazineName = 'Beautiful Birds'
GROUP BY magazineName;
-- You can add magazineName because the WHERE does limit it to that magazine

-- Now how do I see subscribers to all magazines?

-- What would I add to see just magazines with 2 or more subscribers?

-- What about using COUNT(*)

-- What is the total revenue for each magazine?


-- Switch to the bike database

-- Get the highest and lowest priced bike in each brand

-- note Windows machines might let you see brand_name even if you take off the GROUP BY -- it shouldn't


-- How many bikes we have total in stock everywhere. 13,511

-- How can we group it to see how many of each bike we have in stock everywhere?

-- We can also see how many we have at of each bike at each store

-- Do it WITH ROLLUP = shows a total of each bike at the stores and grand total at bottom 13,511

-- If we reverse the grouping with store name as group and product as the sub group we get the total of how many bikes we have at each store.

-- Now we can see if one specific bike is at any of the stores adding a WHERE

