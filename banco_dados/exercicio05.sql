-- CRUD
-- C - CREATE
-- R - READ
-- U - UPDATE
-- D - DELETE
CREATE DATABASE teste;

CREATE TABLE alunos (
	id_aluno INT,
	nome_aluno VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	PRIMARY KEY (id_aluno)
);

CREATE TABLE cursos (
	id_curso INT,
	nome_curso VARCHAR(100) NOT NULL,
	preco_curso NUMERIC(10, 2) NOT NULL,
	PRIMARY KEY (id_curso)
);

CREATE TABLE matriculas (
	id_matricula INT,
	id_aluno INT NOT NULL,
	id_curso INT NOT NULL,
	data_cadastro date NOT NULL,
	PRIMARY KEY (id_matricula),
	FOREIGN key (id_aluno) REFERENCES alunos (id_aluno),
	FOREIGN key (id_curso) REFERENCES cursos (id_curso)
);

INSERT INTO
	alunos (id_aluno, nome_aluno, email)
VALUES
	(1, 'Pedro', 'pedro@gmail.com'),
	(2, 'Ana', 'ana@gmail.com'),
	(3, 'Maria', 'maria@gmail.com'),
	(4, 'Joao', 'joao@gmail.com'),
	(5, 'Thiago', 'thiago@gmail.com'),
	(6, 'Lucas', 'lucas@gmail.com'),
	(7, 'Matheus', 'matheus@gmail.com');

INSERT INTO
	cursos (id_curso, nome_curso, preco_curso)
VALUES
	(1, 'Excel', 800),
	(2, 'Power BI', 500),
	(3, 'VBA', 750),
	(4, 'Python', 1200);

INSERT INTO
	matriculas (id_matricula, id_aluno, id_curso, data_cadastro)
VALUES
	(1, 1, 1, '2023-05-22'),
	(2, 1, 2, '2023-05-22'),
	(3, 2, 3, '2023-05-22'),
	(4, 3, 1, '2023-05-22'),
	(5, 4, 1, '2023-05-22'),
	(6, 4, 1, '2023-05-22');

SELECT
	matriculas.id_matricula,
	matriculas.id_aluno,
	alunos.nome_alunos
FROM
	matriculas
	INNER JOIN alunos ON matriculas
	-- DROP - permite apagar o banco de dados criado
DROP DATABASE teste;

-- Tipo de dados
-- INT
-- NUMERIC(M,D)
-- VARCHAR(N)
-- DATE ano-mes-dia
-- TIMESTAMP - acrescenta hora-minuto-segundo
-- UPDATE - troca o valor da coluna
UPDATE cursos
SET
	preco_curso = 900
WHERE
	id_curso = 4;

-- DELETE - remove a coluna com a matricula
DELETE FROM matriculas
WHERE
	id_matricula = 6;

-- Exercícios:
-- Realizar a criação de um banco de dados para armazenar os dados de um mercado
-- O banco deve ter as seguintes tabelas:

-- produtos -> id_produto, nome_produto, categoria, preco_unitario, quantidade;
-- clientes -> id_cliente, nome_cliente, telefone, email, endereco;
-- vendedor -> id_vendedor, nome_vendedor, telefone, email, endereco;
-- vendas -> id_venda, id_vendedor, id_cliente, id_produto, quantidade_vendida, valor_venda, data_venda;

-- Crie as tabelas utilizando as constraits de not null, primary key e foreign KEY,
-- Preencha os dados de cada tabela com dados fictícios;

CREATE DATABASE mercado;

CREATE TABLE produtos (
	id_produto INT,
	nome_produto VARCHAR(100) NOT NULL,
	categoria VARCHAR(20) NOT NULL,
	preco_unitario NUMERIC(10, 2) NOT NULL,
	quantidade INT NOT NULL,
	PRIMARY KEY (id_produto)
);

CREATE TABLE clientes (
	id_cliente INT,
	nome_cliente VARCHAR(100) NOT NULL,
	telefone VARCHAR(24) NOT NULL,
	email VARCHAR(100),
	endereco VARCHAR(150) NOT NULL,
	PRIMARY KEY (id_cliente)
);

CREATE TABLE vendedor (
	id_vendedor INT,
	nome_vendedor VARCHAR(100) NOT NULL,
	telefone VARCHAR(24) NOT NULL,
	email VARCHAR(100),
	endereco VARCHAR(150) NOT NULL,
	PRIMARY KEY (id_vendedor)
);

CREATE TABLE vendas (
	id_vendas INT,
	id_vendedor INT NOT NULL,
	id_cliente INT NOT NULL,
	id_produto INT NOT NULL,
	quantidade_vendida INT NOT NULL,
	valor_venda INT NOT NULL, -- NUMERIC
	data_venda date NOT NULL,
	PRIMARY KEY (id_vendas),
	FOREIGN key (id_vendedor) REFERENCES vendedor (id_vendedor),
	FOREIGN key (id_cliente) REFERENCES clientes (id_cliente),
	FOREIGN key (id_produto) REFERENCES produtos (id_produto)
);

INSERT INTO
	produtos (id_produto, nome_produto, categoria, preco_unitario, quantidade)
VALUES
	(1, 'salgadinho', 'alimento', 12, 200 ),
	(2, 'leite condensado', 'alimento', 7, 400 ),
	(3, 'notebook', 'eletronico', 2400, 350),
	(4, 'farinha de arroz', 'alimento', 16, 250),
	(5, 'coca', 'bebida', 4, 500);

INSERT INTO
	clientes (id_cliente, nome_cliente, telefone, email, endereco)
VALUES
	(1, 'Davi', '1298765-5432', 'davi@gmail.com', 'rua:..., 435'),
	(2, 'José', '1299888-5566', 'jose@gmail.com', 'rua:..., 363'),
	(3, 'Marcos', '1298667-5555', 'marcos@gmail.com', 'rua:..., 567'),
	(4, 'Antônio', '1298888-7777', 'antonio@gmail.com', 'rua:..., 479');

INSERT INTO
	vendedor (id_vendedor, nome_vendedor, telefone, email, endereco)
VALUES
	(1, 'Francis', '129777-5555', 'francis@gmail.com', 'rua:..., 497'),
	(2, 'Ronaldo', '129222-3333', 'ronaldo@gmail.com', 'rua:..., 703'),
	(3, 'Gustavo', '129333-4444', 'gustavo@gmail.com', 'rua:..., 937');

INSERT INTO 
	vendas (id_vendas, id_vendedor, id_cliente, id_produto, quantidade_vendida, valor_venda, data_venda) 
VALUES
	(1, 1, 2, 4, 8, 128, '2025-07-20'),
	(2, 3, 1, 3, 3, 7200, '2025-06-25'),
	(3, 1, 3, 1, 10, 120, '2025-07-12'),
	(4, 2, 4, 5, 20, 80, '2025-07-17');

