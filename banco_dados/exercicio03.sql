/*SELECT
AVG(unit_price) 
MAX(unit_price)
MIN(unit_price)
FROM
products;*/
/*SELECT DISTINCT
country,
COUNT(*)
FROM
customers
GROUP BY
country;*/
-- Filtros: WHERE, HAVING
/*SELECT DISTINCT
country,
COUNT(*)
FROM
customers
WHERE 
contact_title = 'Owner'
GROUP BY
country;*/
-- HAVING
/*SELECT DISTINCT
country,
COUNT(*)
FROM
customers

GROUP BY
country
HAVING
COUNT(*) > 10;*/
-- Exercícios:
-- Realizar a contagem de produtos por categoria.
SELECT
	category_id
	COUNT(product_id)
FROM
	products
GROUP BY
	category_id

-- Realizar o calculo de preço médio dos produtos por fornecedor.
SELECT
	supplier_id,
	AVG(unit_price)
FROM
	products
GROUP BY
	supplier_id;

-- Realizar o calculo da quantidade total vendida por produto.
SELECT
	product_id,
	SUM(unit_price)
FROM
	order_details
GROUP BY
	product_id
	-- Listar as categorias com mais de 10 produtos em estoque.
SELECT
	category_id,
	COUNT(units_in_stock)
FROM
	products
GROUP BY
	category_id
HAVING
	COUNT(units_in_stock) > 10;

-- Realizar o calculo de media de preço dos produtos por categoria.
SELECT
	category_id,
	AVG(unit_price)
FROM
	products
GROUP BY
	category_id;