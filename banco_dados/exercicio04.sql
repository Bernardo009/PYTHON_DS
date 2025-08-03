-- tabela dimensão
-- tabela fato
-- cardinalidade
-- chave primaria
-- chave estrangeira
-- INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN
SELECT
	product_id,
	quantity
FROM
	order_details;

SELECT
	product_id,
	product_name
FROM
	products;

SELECT
	*
FROM
	order_details
	LEFT JOIN products ON order_details.product_id = products.product_id;

SELECT
	order_details.product_id,
	order_details.quantity,
	products.product_name
FROM
	order_details
	INNER JOIN products ON order_details.product_id = products.product_id;

SELECT
	products.product_id,
	products.product_name,
	products.category_id,
	categories.category_name
FROM
	products
	INNER JOIN categories ON products.category_id = categories.category_id;

-- Exercícios:
-- Crie uma consulta que mostre os nomes dos produtos e os nomes das empresas que os fornecem.
SELECT
	products.product_name,
	suppliers.company_name
FROM
	products
	INNER JOIN suppliers ON products.supplier_id = suppliers.supplier_id;

-- Escreva uma consulta que exiba os nomes dos clientes e os nomes dos funcionários responsáveis por cada pedido.
SELECT
	customers.contact_name,
	employees.first_name,
	orders.order_id
FROM
	orders
	INNER JOIN customers ON customers.customer_id = orders.customer_id
	INNER JOIN employees ON employees.employee_id = orders.employee_id;

-- Escreva uma consulta que mostre os nomes dos clientes e as datas dos pedidos que eles realizaram.
SELECT
	customers.contact_name,
	orders.order_date
FROM
	customers
	INNER JOIN orders ON customers.customer_id = orders.customer_id;