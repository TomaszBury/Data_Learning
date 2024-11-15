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