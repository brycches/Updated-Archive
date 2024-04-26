USE bike;
SELECT SUM(quantity) as "total stock"
FROM stock;

SELECT s.store_name, COUNT(*) AS "number to be reordered"
FROM store s
JOIN stock st ON s.store_id = st.store_id
WHERE st.quantity = 0
GROUP BY s.store_name;
    
SELECT c.category_name, SUM(sc.quantity) AS instock
FROM category c
JOIN product p ON c.category_id = p.category_id
JOIN stock sc ON p.product_id = sc.product_id
JOIN store sr ON sc.store_id = sr.store_id
WHERE sc.quantity > 0 AND sr.store_name = "Baldwin Bikes"
GROUP BY c.category_name
ORDER BY instock;

USE employees;
SELECT COUNT(emp_no) AS "Number of Managers"
FROM dept_manager;

SELECT d.dept_name, FORMAT(AVG(s.salary),2) AS "average salary"
FROM departments d
JOIN dept_emp de ON d.dept_no = de.dept_no
JOIN salaries s ON de.emp_no = s.emp_no
GROUP BY d.dept_name
HAVING AVG(s.salary) > 60000;
    
SELECT d.dept_name, FORMAT(COUNT(e.emp_no),0) AS "Number of Females"
FROM departments d
JOIN dept_emp de ON d.dept_no = de.dept_no
JOIN employees e ON de.emp_no = e.emp_no
WHERE e.gender = 'F'
GROUP BY d.dept_name
ORDER BY COUNT(e.emp_no) DESC;
