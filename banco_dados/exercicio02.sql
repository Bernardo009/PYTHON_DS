-- FILTROS
/*
SELECT * FROM customers where contact_title = 'owner';

select * from products where units_in_stock = 0;

select * from orders where order_date > '1998-01-01';

select * from customers where contact_title = 'Owner' and country = 'France';

select * from customers where country = 'Mexico' or country = 'France';

select * from products where quantity_per_unit like '%boxes%';

select * from customers where country in('Mexico', 'UK', 'Canada');

select * from products where unit_price between 50 and 100;*/

-- exercícios:

-- Liste os produtos onde o preço é maior que 50 
select product_name, unit_price from products where unit_price > 50

-- Liste somente os produtos onde a categoria é Beverages
select product_name, category_id from products WHERE category_id = 1

-- Exiba somente os clientes onde a cidade seja London
select contact_name, city from customers where city = 'London';

-- Liste os funcionarios contratados após 'janeiro de 1994'
select first_name, hire_date from employees where hire_date > '1994-01-31'

-- Liste apenas os produtos que começam com a letra 'C'
select product_name from products where product_name like 'C%'