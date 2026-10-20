SELECT
product,
SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;

SELECT SUM(revenue) AS overall_revenue
FROM sales;