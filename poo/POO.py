# POO

# conceitos principais

# classe - molde
# objetos - instancia da classe
# atributos - caracteristicas do objeto
# metodos - ação que o objetos pode executar
# self - referencia o proprio objeto
# _init_ - metodo contrutor

class Pessoa():

    def __init__(self, nome, idade, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.sexo = sexo

    def _str_(self):
        return f"O nome da pessoa é {self.nome}"

def ap(self):
    print(f"O meu nome é {self.nome} e a minha idade é {self.idade} ")


# instancia
pessoa1 = Pessoa(nome="João", idade=25, altura=1.75, sexo="Masculino")

pessoa1.ap()

pessoa2 = Pessoa("Maria", 15)

print(pessoa1.idade)
print(pessoa1.nome)


# Atributos de classes

 class Livro:
    biblioteca = "Biblioteca Central"

    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")

print(livro1.titulo)
print(livro2.titulo)

print(livro1.biblioteca)
print(livro2.biblioteca)

# Atributos de Instancia
def _init_(self, nome, idade)

#  Atributos de instancia


# Encapsulamento (no python so funciona com métodos)

# _ = protegido

# __ = privado

# metodos

# _ = protegido
# __ = privado

class Livro:
    biblioteca = "Biblioteca Central"

    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.ano = 1985


    def __msg(self):
        print("Texto")

livro1 = Livro("1984", "George Orwell")

livro1.__msg()


# Métodos estaticas (esta vinculado a propria classe)

class Pessoa():
    @staticmethod
    def msg():

Pessoa.msg()

# Objetos e instancia como paramentro (cria uma classe e vincula ela a outra classe)

class Pessoa:
    def _init_(self, nome):
        self.nome = nome

class Mensagem:
    def enviar_mensagem(self, pessoa):
        print(f"Enviando mensagem para {pessoa.nome}")

pessoa1 = Pessoa("Pedro")

msg = Mensagem()

msg.enviar_mensagem(pessoa1)


# Docstring

class Pessoa:
    """
    Representa uma pessoa com nome e idade.

    Atributos:
        nome (str): O nome da pessoa
        idade (int): A idade da pessoa

    Métodos:
        apresentar(): Exibe as informações das pessoas

    """

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def apresentar(self):
        return f"Nome: {self.nome} \nIdade: {self.idade}"


# Relação entre classes (uma classe dentro de outra classe)
# associação - uma classe usa outra, mas sem pertencer a ela

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Leitor:
    def Ler(self, Livro):
        self.Livro = Livro
        print(f"")


# Agregação - Uma classe contem outra, mas cada uma vive separadamente


# Composição - Uma classe contem outra, mas depende dela pra existir


# Herança - Uma classe herda atributos e metodos de outra classe


# Modularização
# subclasse, herança e super

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibir_dados(self)
        return f"Nome: {self.nome} \nSobrenome: {self.sobrenome} "


class Aluno(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)


# Polimorfismo

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibir_dados(self)
        return f"Nome: {self.nome} \nSobrenome: {self.sobrenome} "

    def falar(self):
        print("Olá")

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)

    def falar(self):
        print("Hallo!")
