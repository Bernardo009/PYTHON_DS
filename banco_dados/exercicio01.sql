-- Ordenação

-- SELECT * FROM customers order by contact_name desc;

-- Liste todos os produtos disponíveis
SELECT product_name FROM products;

-- Mostre apenas os nomes e os preços dos produtos
SELECT product_name, unit_price FROM products;

-- Liste os nomes dos clientes da tabela Customers
SELECT contact_name FROM customers;

-- Liste os produtos em ordem decrescente utilizando a coluna de preço
SELECT product_name, unit_price FROM products order by unit_price desc;

-- Liste os clientes em ordem alfabética pelo nome da empresa
SELECT contact_name, company_name FROM customers order by company_name;





