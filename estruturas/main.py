# Faça um programa que receba 5 numeros, armazene-os em uma lista e depois exiba a lista.
# nums = []
# for i in range(1, 6):
#     num = int(input("Digite um número: "))
#     nums.append(num)


# print(f"A lista é: {lista} ")

# Faça um programa que receba 10 numeros inteiros e armazene-os em uma lista. Armazene os numeros pares na lista pares e os numeros impares na lista impares. Imprima as três lista.

# nums = []
# impares = []
# pares = []

# for i in range(1, 10 + 1):
#     num = int(input("Digite um numero: "))
#     nums.append(num)


#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)

# print(f"Lista de numeros: {nums}\nLista de numeros pares: {pares}\nLista de numeros impares: {impares}")

# Crie um dicionario com informações sobre um livro como ano, autor e gênero, acesse e imprima cada valor usando a chave.

# livro = {"nome":"java",
#                 "ano":1999,
#                 "autor":"Carlos",
#                 "gênero":"programação"}

# print(livro["nome"])
# print(livro["ano"])
# print(livro["autor"])
# print(livro["gênero"])

#

# Crie um dicionario que armazena informaçoes das configuraçoes de um computador, depois utilize a estrutura for para exibir as informaçoes do computador.

# conf = {
#     "cpu": "inte core i7 12500",
#     "RAM": "16GB",
#     "Placa_Mae": "Asus",
#     "ssd": "nvme 256GB",
#     "GPU": "RTX 4070",
# }

# for chave, valor in conf.items():
#     print(f"{chave}:, {valor}")

########################################

# Funções

# def msg():
#     # print("Olá, mundo!");
#     # return 5 + 7

#     return f"A soma entre {5} e {7} é {5 + 7}"

# print(msg())

# Argumento padrão

# def soma(num1=5, num2=2):
#     return num1+num2

# print(soma())

# def regiao(pais="Brasil"):
#     return f"Você está no {pais}"

# print(regiao("Estados Unidos"))

# *Args e **Kwargs

# def soma(*n):

#     soma = 0

#     for i in n:
#         soma += i

#     return f"A soma entre os números {n} é {soma}"

# print(soma(5,7,2,3,9))

# **Kwargs


# def pessoa(**dados):

#     for chave, valor in dados.items():
#         print(f"{chave} da pessoa é {valor}")


# pessoa(nome="pedro", idade=22, altura=1.75)

# Módulos e PIP

# pip

# Ambientes virtuais

# Manipulação de arquivos

# arquivos = open("dados.txt", "r")

# print(arquivos.read())

# print(arquivos.readline())


# arquivos = open("dados.txt", "w")

# arquivos.write("Marcos")


# arquivos.close()
