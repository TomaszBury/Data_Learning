select * from actor limit 10;

select
  *
from
  actor
limit
  10;

  select category_id, count(distinct film_id)
from film_category
group by 1
order by 2 desc;

select title, rental_rate
from film
where rental_rate = 0.99
order by title desc;

select first_name, last_name, email
from customer
where store_id = 2;

select first_name
from actor
where actor_id = 50

select title, rental_rate
from film
where rental_rate = .99;

select count(title)
from film
where rental_rate = .99;

select count(title), rental_rate
from film
group by rental_rate;
-- same as:
select count(title), rental_rate
from film
group by 2;

select film.rating, count(film.rating) as count_rating, inventory.store_id
from film
join inventory 
on film.film_id = inventory.film_id
group by film.rating, inventory.store_id
order by count_rating;

select rating, count(rating) as prevelents,rental_rate
from film
group by rental_rate, rating
order by prevelents;

select rating, count(rating) as count_rating
from film
group by rating
order by count_rating desc

select rating, count(rating) as prevelents,rental_rate
from film
where rental_rate = .99
group by rental_rate, rating
order by prevelents;

select rating, count(rating)
from film
group by rating
order by count(rating) desc;

select rating, rental_rate, count(film_id)
from film
where rental_rate = 0.99
group by rating, rental_rate
order by count(rating) desc;

select
  customer.customer_id,
  customer.first_name,
  customer.last_name,
  address.address
from
  customer
  join address on customer.address_id = address.address_id

  select film.title, film_list.category, language.name
from film
join film_list
on film.film_id = film_list.FID
join language
on film.language_id = language.language_id
order by language.name desc;

select film.title, language.name, category.name as Cat_Name
from film

join film_category
on film.film_id = film_category.film_id

join category
on film_category.category_id = category.category_id

join language
on film.language_id = language.language_id;

select film.title, count(rental.inventory_id) as rented_out
from film

join inventory
on film.film_id = inventory.film_id

join rental
on inventory.inventory_id = rental.inventory_id

group by film.title

order by rented_out desc, title

-- revenue by video title
-- revenue = price * number of rentals

select film.title, count(rental.inventory_id), film.rental_rate ,count(rental.inventory_id) * film.rental_rate as Revenue
from film

join inventory
on film.film_id = inventory.film_id

join rental
on inventory.inventory_id = rental.inventory_id

group by film.title

order by Revenue desc

-- What customer has paid us the most money

select customer.first_name, customer.last_name, count(rental.customer_id) * film.rental_rate as value_of_customer
from customer

join rental
on customer.customer_id = rental.customer_id

join inventory
on rental.inventory_id = inventory.inventory_id

join film
on inventory.film_id = film.film_id

group by customer.customer_id

order by value_of_customer desc

-- what customer has paid us the most money

select customer.first_name, customer.last_name, sum(payment.amount) as total_sales
from customer

join payment
on customer.customer_id = payment.customer_id

group by customer.customer_id

order by total_sales desc

-- what store has historically brought the most revenue?

select address.address, sum(payment.amount) as revenue_by_store
from store

join address
on store.address_id = address.address_id

join customer
on store.store_id = customer.store_id

join payment
on customer.customer_id = payment.customer_id

group by store.store_id

order by revenue_by_store desc

-- what store has historically brought the most revenue?

select store.store_id, sum(payment.amount) as revenue_by_store
from store

join inventory
on store.store_id = inventory.store_id

join rental
on inventory.inventory_id = rental.inventory_id

join payment
on rental.rental_id = payment.rental_id

group by store.store_id

order by revenue_by_store desc

-- How many rental we had each month
select count(rental_id),EXTRACT(MONTH FROM rental_date) AS Month
from rental
group by Month

select count(rental_id),left(rental_date,7) AS Month
from rental
group by Month
order by count(rental_id)

select film.title, max(rental.rental_date), min(rental.rental_date)
from rental
join inventory
on rental.inventory_id = inventory.inventory_id
join film
on inventory.film_id = film.film_id
group by film.film_id

-- cutomers who have been inavtive
-- what customers havent rented a movie in the last month
select
  customer.first_name,
  customer.last_name,
  extract(
    MONTH
    FROM
      rental.rental_date
  ) as rental_date
from
  customer
  join rental on customer.customer_id = rental.customer_id

  -- evry customers last rental date
select customer.first_name, customer.last_name, max(extract(month from rental.rental_date)) as last_rental
from customer

join rental
on customer.customer_id = rental.customer_id
-- where customer.last_name = "ROUSH"

group by customer.customer_id
order by last_rental desc


-- revenue by month
select extract(month from payment_date) as payment_month, sum(amount)
from payment
group by payment_month

-- evry customers last rental date
select
  concat(customer.first_name, " ", customer.last_name) as name,
  customer.email as email,
  max(
        rental.rental_date

  ) as last_rental
from
  customer
  join rental on customer.customer_id = rental.customer_id -- where customer.last_name = "ROUSH"
group by
  customer.customer_id
order by
  last_rental desc
  
-- revenue by month

select
  concat(year(payment_date),"-",lpad(month(payment_date),2,"0")) as payment_month,
  sum(amount)
from
  payment
group by
  payment_month


-- revenue by month

select
  DATE_FORMAT(payment_date, '%Y-%m') as payment_month,
  sum(amount)
from
  payment
group by
  payment_month

  -- How many distinct renters per month

select count(distinct(customer.customer_id)) as unique_renters, DATE_FORMAT(rental_date, '%Y-%m') as rental_d,
count(rental.rental_id) as total_rentals,
count(rental.rental_id) / count(distinct customer.customer_id) as qvg_num_rentals_per_renter
from customer

join rental
on customer.customer_id = rental.customer_id

group by rental_d
-- the number of distinct films rented each month
select
  count(distinct film.film_id) as distinct_films,
  DATE_FORMAT(rental.rental_date, '%Y-%m') as rent_date
from
  film
  join inventory on film.film_id = inventory.film_id
  join rental on inventory.inventory_id = rental.inventory_id
  
group by rent_date

-- in comparison opertors having

-- number of rentals in the comedy sports and family

select category.name, count(rental.rental_id) as num_rentals
from rental

join inventory
on rental.inventory_id = inventory.inventory_id

join film_category
on inventory.film_id = film_category.film_id

join category
on film_category.category_id = category.category_id

where category.name in ("Comedy" , "Sports" , "Family")

group by category.name
-- comparison operators


select category.name, count(rental.rental_id) as num_rentals
from rental

join inventory
on rental.inventory_id = inventory.inventory_id

join film_category
on inventory.film_id = film_category.film_id

join category
on film_category.category_id = category.category_id

where category.name != "Comedy"

group by category.name

-- comparison operators

-- users who have rented at least 3 times

select customer.first_name, customer.last_name, count(rental.rental_id) as num_rentals
from customer

join rental
on customer.customer_id = rental.customer_id

group by customer.customer_id

HAVING COUNT(rental.rental_id) > 3;

-- how much revenue has one single store made over PG-13 and R-rated films.

select sum(payment.amount) as revenue, film.rating,customer.store_id
from payment

join customer
on payment.customer_id = customer.customer_id

join rental
on payment.rental_id = rental.rental_id

join inventory
on rental.inventory_id = inventory.film_id

join film
on inventory.film_id = film.film_id


where film.rating in ("PG-13" , "R") and customer.store_id = "1"

group by film.rating,customer.store_id

-- how much revenue has one single store made over PG-13 and R-rated films.

select sum(payment.amount) as revenue, film.rating, inventory.store_id
from payment

join rental
on payment.rental_id = rental.rental_id

join inventory
on rental.inventory_id = inventory.inventory_id

join film
on inventory.film_id = film.film_id


where film.rating in ("PG-13" , "R") and inventory.store_id = "1"

group by film.rating, inventory.store_id

-- how much revenue has one single store made over PG-13 and R-rated films.

select sum(payment.amount) as revenue, film.rating, inventory.store_id
from payment

join rental
on payment.rental_id = rental.rental_id

join inventory
on rental.inventory_id = inventory.inventory_id

join film
on inventory.film_id = film.film_id


where film.rating in ("PG-13" , "R") and inventory.store_id = "1"
and rental.rental_date between '2005-06-08' and '2005-07-19'

group by film.rating, inventory.store_id

-- rentals per customer
select
  rentals_per_customer.num_rentals, 
  count(distinct rentals_per_customer.customer_id) as num_customers,
  sum(payment.amount) as total_revenue
from 
  (
    select
      rental.customer_id, count(distinct rental.rental_id) as num_rentals
      from rental
    group by rental.customer_id
  ) as rentals_per_customer 
  join payment on rentals_per_customer.customer_id = payment.customer_id

where rentals_per_customer.num_rentals > 20

group by rentals_per_customer.num_rentals

order by num_customers desc;
-- Create a temporary table with rental counts per customer
CREATE TEMPORARY TABLE rpc AS
SELECT rental.customer_id, COUNT(DISTINCT rental.rental_id) AS num_rentals
FROM rental
GROUP BY rental.customer_id;

-- Calculate total revenue for customers with more than 20 rentals
SELECT SUM(payment.amount) AS total_rev
FROM rpc
JOIN payment ON rpc.customer_id = payment.customer_id
WHERE rpc.num_rentals > 20;


