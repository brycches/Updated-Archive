USE magazine;

-- q1
SELECT magazineName, ROUND((magazinePrice*.93), 2)AS '7% off'
FROM magazine;

SELECT * FROM subscriber;

-- q2
SELECT subscriberKey, ROUND(DATEDIFF('2023-07-07', subscriptionStartDate)/365)AS 'years since subscription'
FROM subscription;

-- q3
SELECT DATE_FORMAT(subscriptionStartDate, '%M %D, %Y') AS subscriptionStartDate , subscriptionLength, DATE_FORMAT(DATE_ADD(subscriptionStartDate, INTERVAL subscriptionLength MONTH), '%M %D, %Y') AS 'subscription end'
FROM subscription;

USE bike;
-- q4
SELECT product_name
FROM product;

SELECT SUBSTRING_INDEX(product_name, ' - ', 1) AS 'Product Name w/o Year'
FROM product
ORDER BY product_id desc
LIMIT 14;
-- substring index function

-- q5
-- format
SELECT product_name, CONCAT('$', format(list_price, 2)), CONCAT('$', FORMAT(list_price * 0.05, 2)) AS '5% down', CONCAT('$', FORMAT((list_price - (list_price * 0.05)) * 0.1, 2)) AS '10 equal payments'
FROM product
WHERE product_name like '%2019%';
