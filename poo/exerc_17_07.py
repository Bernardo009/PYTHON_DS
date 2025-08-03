# Crie uma classe produto com os atributos nome, preco e quantidade. Implemente o método _str_ para exibir os dados do produto.


class Produto():

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"""
O nome do produto: {self.nome}\n
O preço do produto: {self.preco}\n
A quantidade de produtos: {self.quantidade}"""


produto1 = Produto(nome="Caneta", preco=5.00, quantidade=1500 )

print(produto1)


# Crie uma classe livro com os atributos titulo, autor, nome e ano_publicaçao. Adicione um metodo exibir_detalhes que exiba todas as informaçoes do livro.

class Livro():

    def __init__(self, titulo, autor, nome, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.nome = nome
        self.ano_publicacao = ano_publicacao

    def __exibir_detalhes__(self):
        return f"""
O nome é {self.nome}\n
O titulo é {self.titulo}\n
O autor é {self.autor}\n
ano_publicação é {self.ano_publicacao}
"""

livro1 = Livro("O hobbit", "O hobbit", "J.R.R.Tolkin", 1937)

print(livro1.__exibir_detalhes__())


# Crie uma classe itemcarrinho com os atributos nome, preco_unitario e quantidade. Adicione um método calcular_total que retorna o valor total do item com base no preço e quantidade

class ItemCarrinho():

    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    def __calcular_total__(self):
        return f"Valor tatal: R${self.preco_unitario*self.quantidade:.2f}"


item1 = ItemCarrinho(nome="Arroz", preco_unitario=22.80, quantidade=200):

print(item1.__calcular_total__())
