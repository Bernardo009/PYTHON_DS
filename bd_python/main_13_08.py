# Integração do python com banco de dados
# sqlite
import sqlite3

connection = sqlite3.connect("database.db")

# Criar a tabela
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE movies(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               ano INTEGER NOT NULL,
               nota REAL NOT NULL
               )

"""
)

print("Tabela criada com sucesso!")

connection.close()

# Inserir dados na tabela
# INSERT INTO - commit
cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO movies(nome, ano, nota)
    VALUES('Star Wars', '1980', '10')

"""
)

cursor.execute(
    """
    INSERT INTO movies(nome, ano, nota)
    VALUES('Harry Potter', '2001', '9.5')

"""
)

cursor.execute(
    """
    INSERT INTO movies(nome, ano, nota)
    VALUES('O Senhor dos Anéis', '2001', '10')

"""
)

connection.commit()

print("Dados inseridos com sucesso!")

connection.close()


# Acrescenta um item novo na tabela,
cursor = connection.cursor()

nome = input("Digite o nome do filme: ")

ano = int(input("Digite o ano do filme: "))

nota = float(input("Digite a nota do filme: "))

cursor.execute(
    """
    INSERT INTO movies(nome, ano, nota)
    VALUES( ?, ?, ?) 
""",
    (nome, ano, nota),
)  # criar uma tupla

connection.commit()

print("Dados inseridos com sucesso!")

connection.close()


# Exibir as linhas do banco de dados utilizando as ferramentas fetchall e For
cursor = connection.cursor()

query = cursor.execute("SELECT nome, ano, nota FROM movies")

print(query.fetchall())

for linha in cursor.execute("SELECT * FROM movies"):
    print(linha)

for linha in cursor.execute("SELECT * FROM movies ORDER BY nota DESC"):
    print(linha)

connection.close()

# Atualizar nome e id utilizando a ferramenta UPDATE e WHERE
cursor = connection.cursor()

id = int(input("Digite o id do filme que deseja atualizar: "))

nome = input("Informe o novo nome do filme: ")

cursor.execute(
    """
    UPDATE movies set nome = ?
    WHERE id == ?
""",
    (nome, id),
)  # recebe uma tupla

connection.commit()

print("Dados atualizados com sucesso!")

connection.close()


# Remover filme utilizando DELETE
cursor = connection.cursor()

id = int(input("Digite o id do filme que deseja atualizar: "))

cursor.execute(
    """
    DELETE movies
    WHERE id == ?
""",
    (id),
)  # recebe uma tupla

connection.commit()

print("Filme removido com sucesso!")

connection.close()
