-- number 1
USE v_art;
INSERT into artist (artist_id, fname, mname, lname, dob, dod, country, local)
	VALUES (10, 'Gustav', null,'Klimt','1862','1917','Italy','n' );
    
-- number 2 
SELECT fname, mname, lname, dob, dod, country, local
FROM artist
order by lname;

-- number 3
UPDATE artist
SET dod=1918
WHERE artist_id = 10;

-- number 4
DELETE 
FROM artist 
WHERE artist_id = 10;

USE bike;
-- number 5
SELECT first_name, last_name, phone
FROM customer 
WHERE city = 'Buffalo';

-- number 6
SELECT product_name, list_price, list_price-600 AS discount_price
FROM product 
WHERE list_price > 6000 
ORDER BY list_price desc;

-- number 7
SELECT first_name, last_name, email
FROM staff
WHERE store_id = 2;

-- number 8
SELECT product_name, model_year, list_price
FROM product
WHERE product_name LIKE '%CrossRip%';

-- number 9
SELECT product_name, list_price
FROM product
WHERE list_price < 750 AND list_price > 600
ORDER BY list_price;

-- number 10
SELECT first_name, last_name, phone, street, city, state, zip_code
FROM customer
WHERE (phone IS NOT null AND (city LIKE '%los%' OR city LIKE '%lan%')) OR last_name = 'Armstrong' LIMIT 5;