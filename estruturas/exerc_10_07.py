# Crie um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja invalido e continue pedindo até que o usuário informe um valor válido

nota = float(input("Digite uma nota entre zero e dez: \n"))

while True:
    if nota >= 0 and nota <= 10:
        print("O valor digitado estava entre 0 e 10")
        break
    else:
        print("Valor invalido")

# Faça um programa que leia 5 numeros e informe a soma e a media dos números

soma = 0

for i in range(1, 5 + 1):
    num = int(input(f"Digite o {i} numero: "))

    soma += num

    media = soma / i

print(f"A soma dos valores é: {soma} \nA media dos valores é: {media}")

# Crie um programa em python que conte quantas vezes a letra "a" (maiuscula ou minuscula) aparece na frase "A pratica leva à perfeição"

frase = "A pratica leva a perfeição"

qtd = 0

for letra in frase:
    if "a" in letra.lower():
        qtd += 1

print(f"")

# Crie um programa que realize uma contagem regressiva iniciando em 10 e terminando em 0 utilizando o while

cont = 10

while cont >= 0:
    print(cont)
    cont -= 1
