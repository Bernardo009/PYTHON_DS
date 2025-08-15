import psycopg2

connection = psycopg2.connect(
    database="northwind",
    user="postgres",
    password="",
    host="localhost",
    port="",
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

resultado = cursor.fetchall()

print(resultado)
