##SQL Exercises
##Query1
##  Write the SQL to generate a report of the total quantity and amount paid
##  for each purchase.  The result should have the following columns.
##  (Difficulty Easy)
##  columns:  customer_id, first_name, last_name, email, purchase_id, purchase_time
##  total_quantity, total_amount_paid


##Query 1 Solution:
SELECT c.customer_id, c.first_name, c.last_name, c.email,
p.purchase_id, p.purchase_time, SUM(pi.quantity) as total_quantity,
SUM(pi.total_amount_paid) as total_amount_paid
FROM customer c
INNER JOIN purchase p
ON c.customer_id = p.customer_id
INNER JOIN purchase_item pi
ON p.purchase_id = pi.purchase_id
GROUP BY c.customer_id, p.purchase_id
ORDER BY c.customer_id

##Query 1 Result:
customer_id	first_name	last_name	email	         purchase_id	purchase_time	total_quantity	total_amount_paid
1	         James	    Smith	jamessmith@example.com	100	2019-06-14T15:42:11.403244Z	  6	        302.5
1	         James	    Smith	jamessmith@example.com	101	2019-06-14T15:42:11.403344Z	  1	        40
1	         James	    Smith	jamessmith@example.com	102	2019-06-14T15:42:11.403348Z	  1	        1995
2	         Mary	    Johnson	maryjohnson@example.com	103	2019-06-14T15:42:11.403351Z	    4	    4190
3	         John	   Williams johnwilliams@example.com 104	2019-06-14T15:42:11.403353Z	1	    60
5  	         Michael	Garcia	michaelgarcia@example.com 105	2019-06-14T15:42:11.403355Z	1	    400

##Query 2
##  Write the SQL to generate a report of customers who have made more than 1
##  purchase, sorted by teh total number of purchases in descending order.
##  The result should have the following columns.
##  (Difficulty Medium)
## columns:  customer_id, first_name, last_name, email, number_of_purchases

##Query 2 Solution
SELECT c.customer_id, c.first_name, c.last_name, c.email,
COUNT(p.purchase_id) as number_of_purchases
FROM customer c
INNER JOIN purchase p
ON c.customer_id = p.customer_id
GROUP BY c.customer_id
HAVING COUNT(p.purchase_id) > 1
ORDER BY number_of_purchases DESC

##Query 2 Result:
customer_id	first_name	last_name	   email	          number_of_purchases
1	          James	      Smith	  jamessmith@example.com	     3

##Query 3
##  Write the SQL to generate a report of the number of customers who have
##  purchased each sku.  Any skus with no purchases don't need to be included in
## the report.  The result should have the resulting columns.
##  (Difficulty Medium)
##  columns: sku, total_number_of_customers

##QUERY 3 Solution:
SELECT sku, COUNT(p.customer_id) as total_number_of_customers
FROM purchase_item pi
INNER JOIN purchase p
ON pi.purchase_id = p.purchase_id
GROUP BY sku
HAVING COUNT(p.customer_id) > 0
ORDER BY total_number_of_customers DESC

##Query 3 Result:
sku	        total_number_of_customers
bike	               2
shoe_wht_39	           1
headphones	           1
shorts	               1
shirt	               1
shoe_blk_42	           1
shoe_lace_white	       1

##Query 4
##  Write the SQL to generate a report of all customers and the total amount
##  they've spent.  Users who haven't made any purchases should still be included
##  in the report.
## (Difficulty Medium)
##  columns: customer_id, first_name, last_name, email, total_amount_paid

##Query 4 Solution:
SELECT c.customer_id, first_name, last_name, email, SUM(total_amount_paid)
FROM customer c
LEFT JOIN purchase p
ON c.customer_id = p.customer_id
LEFT JOIN purchase_item pi
ON p.purchase_id = pi.purchase_id
GROUP BY c.customer_id

##Query 4 Result:
customer_id	first_name	last_name	email	             total_amount_paid
1	        James	   Smith	jamessmith@example.com	       2337.5
3           John	   Williams johnwilliams@example.com	   60
4	        Patricia   Brown	patriciabrown@example.com	   (null)
2	        Mary	   Johnson	maryjohnson@example.com	       4190
5	        Michael	   Garcia	michaelgarcia@example.com	   400

##Query 5
##  Write the SQL to show some basic statistics about two types of purchases:
##  Those that include a bike (as a purchase_item with sku='bike') and those that
##  do not.  For these two cases, we're interested in knowing how many purchases
## there are, the average amount paid across those purchases (known as AOV for
##  "average order value"), and the average number of items in each purchase.
##  The result should be two rows with the following columns.
##  (Difficulty Hard)
##  columns:  purchase_has_bike(boolean), num_purchases, avg_amount_paid, avg_number_of_items

##QUERY 5 Solution
SELECT CASE WHEN(sku = 'bike') THEN 'TRUE' else 'False' END as purchase_has_bike,
COUNT(purchase_id) as num_purchases, AVG(total_amount_paid) as avg_amount_paid,
AVG(quantity) as avg_number_of_items
FROM purchase_item
GROUP BY purchase_has_bike

##Query 5 Result:
purchase_has_bike	num_purchases	avg_amount_paid	    avg_number_of_items
TRUE	               2	          2992.5	         1.5
False	               6	         167.08333333333334	 1.8333333333333333


##Query 6
##  Write the SQL to generate a report of the most recent purchase made by each
##  customer.  You don't need to include customers who haven't made a purchase.
##  The result should have the following columns.  (Hint:  you can assume the
##  underlying database support window functions.  But it is still poassible without
## window functions.)
##  (Difficulty Hard)
##  columns:  customer_id, first_name, last_name, email, purchase_id, purchase_time,
##  total_quantity, total_amount_paid

##Query 6 Solution (without window function)
select p.customer_id, first_name, last_name, email,
max(p.purchase_id) as purchase_id, max(p.purchase_time) as purchase_time,
sum(pi.quantity) as total_quantity, sum(pi.total_amount_paid) as total_amount_paid
from purchase p
join customer c
on c.customer_id = p.customer_id
join purchase_item pi
on pi.purchase_id = p.purchase_id
group by p.customer_id, c.first_name, c.last_name, c.email

##Query 6 Result:
customer_id	first_name	last_name	email	             purchase_id	purchase_time	      total_quantity	total_amount_paid
1	          James	    Smith	jamessmith@example.com	     102	2019-06-14T19:36:46.652442Z	    8	      2337.5
3	          John	    Williams	johnwilliams@example.com 104	2019-06-14T19:36:46.65245Z	    1	      60
5          	  Michael	Garcia	michaelgarcia@example.com	 105	2019-06-14T19:36:46.652453Z	    1	      400
2	          Mary	    Johnson	maryjohnson@example.com	     103	2019-06-14T19:36:46.652448Z	    4	      4190

##Query 6 Solution with window function:
SELECT *
FROM
(SELECT c.customer_id, first_name, last_name, email,
p.purchase_id, MAX(purchase_time) as purchase_time,
SUM(quantity) OVER(PARTITION BY c.customer_id ORDER BY p.purchase_id) as total_quantity,
SUM(total_amount_paid) OVER(PARTITION BY c.customer_id ORDER BY p.purchase_id) as total_amount_paid
FROM customer c
INNER JOIN purchase p
ON c.customer_id = p.customer_id
INNER JOIN purchase_item pi
ON p.purchase_id = pi.purchase_id
GROUP BY c.customer_id, p.purchase_id, pi.quantity, pi.total_amount_paid) X
WHERE X.purchase_id IN(SELECT MAX(p.purchase_id) FROM customer c
                       INNER JOIN purchase p ON c.customer_id = p.customer_id
                       GROUP BY c.customer_id)

##Query 6 Result:
##(Not optimal, has a duplicate customer_id 102 Mary Johnson... needs tweaking.  Otherwise, result the same as above)
customer_id	first_name	last_name	email	             purchase_id	purchase_time	      total_quantity	total_amount_paid
1	        James	    Smith	jamessmith@example.com	   102	2019-06-14T19:36:46.652442Z	    8	            2337.5
2	        Mary	    Johnson	maryjohnson@example.com	   103	2019-06-14T19:36:46.652448Z	    4	            4190
2	        Mary	    Johnson	maryjohnson@example.com	   103	2019-06-14T19:36:46.652448Z	    4	            4190
3	        John	    Williams johnwilliams@example.com  104	2019-06-14T19:36:46.65245Z	    1	            60
5	        Michael	    Garcia	michaelgarcia@example.com  105	2019-06-14T19:36:46.652453Z	    1	            400
