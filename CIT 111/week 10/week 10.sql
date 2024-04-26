USE v_art;
SELECT w.artfile AS "artfile"
FROM artwork w
JOIN artist i ON w.artist_id = i.artist_id
WHERE i.lname = "Picasso";

SELECT a.artfile AS "artfile"
FROM artwork a
JOIN artwork_keyword ak ON ak.artwork_id = a.artwork_id
JOIN keyword k ON ak.keyword_id = k.keyword_id
WHERE k.keyword LIKE "%land%";

SELECT i.fname AS fname, i.lname AS lname,w.title
FROM artist i
LEFT JOIN artwork w ON i.artist_id = w.artist_id
WHERE w.title IS NULL;

USE magazine;
SELECT m.magazineName, s.subscriberFirstName, s.subscriberLastName
FROM magazine m
LEFT JOIN subscription sk ON m.magazineKey = sk.magazineKey
LEFT JOIN subscriber s ON s.subscriberKey = sk.subscriberKey
WHERE s.subscriberFirstName IS NULL;

SELECT m.magazineName
FROM magazine m
JOIN subscription sk ON m.magazineKey = sk.magazineKey
JOIN subscriber s ON s.subscriberKey = sk.subscriberKey
WHERE s.subscriberFirstName = "Albert";

USE employees;
SELECT e.first_name, e.last_name
FROM employees e
JOIN dept_emp de ON de.emp_no = e.emp_no
JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name = "Marketing"



