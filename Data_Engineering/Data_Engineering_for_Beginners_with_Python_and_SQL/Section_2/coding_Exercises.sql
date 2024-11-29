select count(*) as users_above_50 
from users
where age > 50

SELECT client_id, 
       COUNT(order_id) AS orders,
       AVG(order_amount) AS avg_order
FROM orders
GROUP BY client_id;

SELECT department AS Department,
       AVG(salary) AS "Average Salary"
FROM employees
GROUP BY department
ORDER BY department ASC;

SELECT product_category AS "Product Category", 
       SUM(sales_amount) AS "Total Sales Amount", 
       AVG(sales_amount) AS "Average Sales Amount"
FROM sales
GROUP BY "Product Category"
ORDER BY "Total Sales Amount" DESC;

-- Solution
-- Write your SQL query here to find the highest and lowest salaries by department
WITH HighestSalaries AS (
    SELECT
        department AS "Department",
        first_name || ' ' || last_name AS "Highest Earner",
        MAX(salary) AS "Highest Salary"
    FROM
        employees
    GROUP BY
        department
),
LowestSalaries AS (
    SELECT
        department AS "Department",
        first_name || ' ' || last_name AS "Lowest Earner",
        MIN(salary) AS "Lowest Salary"
    FROM
        employees
    GROUP BY
        department
)
SELECT
    H.Department,
    H."Highest Earner",
    H."Highest Salary",
    L."Lowest Earner",
    L."Lowest Salary"
FROM
    HighestSalaries H
JOIN
    LowestSalaries L
ON
    H.Department = L.Department
ORDER BY
    H.Department ASC;

    -- Solution
-- Write your SQL query here to find the products with the highest and lowest inventory levels
WITH highest as (
SELECT
    product_name AS "Product Name",
    inventory_level AS "Inventory Level"
FROM
    products
ORDER BY
    inventory_level DESC
LIMIT 5
 
), lowest as (
 
SELECT
    product_name AS "Product Name",
    inventory_level AS "Inventory Level"
FROM
    products
ORDER BY
    inventory_level ASC
LIMIT 5
)
SELECT *
FROM (
SELECT * FROM highest
UNION ALL
SELECT * FROM lowest
) ORDER BY `Inventory Level` DESC

SELECT (first_name || ' ' || last_name) AS "Customer Name", 
       SUM(purchase_amount) AS "Total Purchase Amount"
FROM customer_purchases
GROUP BY (first_name || ' ' || last_name)
ORDER BY SUM(purchase_amount) DESC
LIMIT 5;


SELECT product_name AS "Product Name", 
       COUNT(order_id) AS "Order Count"
FROM orders
GROUP BY product_name
ORDER BY COUNT(order_id) DESC
LIMIT 10;


SELECT subject_name AS "Subject Name", 
       AVG(grade) AS "Average Grade"
FROM student_grades
GROUP BY subject_name
ORDER BY AVG(grade) DESC;


SELECT product_category AS "Product Category", 
       COUNT(product_id) AS "Number of Products"
FROM products
GROUP BY product_category
ORDER BY COUNT(product_id) DESC
LIMIT 1;


