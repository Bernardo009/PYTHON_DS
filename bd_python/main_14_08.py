import psycopg2

connection = psycopg2.connect(
    database="teste",
    user="postgres",
    password="SENAISJC2025",
    host="localhost",
    port="5432",
)

# Cria mais duas linhas com novos cursos, utilizando for.
cursor = connection.cursor()

cursos = [
    (5, "Operador de Microcomputador", 590.00),
    (6, "Analista de Lógistica", 450.00),
]

for curso in cursos:
    cursor.execute(
        """
        INSERT INTO cursos(id_curso, nome_curso, preco_curso)
        VALUES (%s, %s, %s)
                    """,
        curso,
    )

connection.commit()

print("Dados inseridos com sucesso!")

connection.close()


# Atualiza para uma nova informação, trocando o nome do curso.
cursor = connection.cursor()

query = """
    UPDATE cursos
    Set nome_curso = %s
    WHERE id_curso = %s
"""

cursor.execute(query, ("Operador de lógistica", 6))

connection.commit()

print("Dados atualizados com sucesso!")

connection.close()

# Uso da ferramenta DELETAR.
cursor = connection.cursor()

query = """
    DELETE FROM cursos
    WHERE id_curso = %s
"""

cursor.execute(query, (6,))

connection.commit()

print("Dado removido com sucesso!")

connection.close()
