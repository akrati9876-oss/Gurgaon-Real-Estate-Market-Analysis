-- What are the 10 most expensive properties in Gurgaon?
select * 
from properties 
order by price 
desc limit 10;

-- Average price by locality
select locality, round(avg(price), 2)
as avg_price
from properties
group by locality
order by avg_price desc
limit 10;  

-- Which BHK configuration is most common?
select bhk_count, count(*) as properties
from properties
group by bhk_count
order by bhk_count;

-- How does property price vary with BHK size ?
select bhk_count, round(avg(price),2)
as avg_price
from properties
group by bhk_count
order by avg_price desc; 

-- Which Gurgaon localities command the highest price/sq.ft ?
select locality,
round(avg(rate_per_sqft),2) as avg_rate
from properties
group by locality
order by avg_rate desc
limit 10;

-- Compare availability and average price between property statuses .
select status, count(*) as properties, round(avg(price),2) as avg_price
from properties
group by status; 

-- Do RERA-approved properties have a higher average price ?
select rera_approval, count(*) as properties, round(avg(price), 2) as avg_price
from properties
group by rera_approval;

-- Which builders are positioned at the premium end of the market ?
select builder_name, round(avg(rate_per_sqft),2) as avg_rate
from properties
group by builder_name
order by avg_rate desc
limit 10;

-- AREA vs PRICE
select area, round(avg(price),2) as avg_price
from properties
group by area
order by area; 
  

 
