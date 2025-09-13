# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(num1, num2, num3):
    return f"A soma dos números: {num1}, {num2}, {num3} é {num1+num2+num3}"

print(soma(5,2,7))

Faça uma função que informe a quantidade de digitos de um determinado número inteiro informado.

def qtd_num(num):

    cont = 0

    for i in str(num):

        cont += 1

    return cont

print(qtd_num(527))

def qtd_num(num):

    return len(str(num))

print(qtd_num(527))

# Crie um programa que funcione como uma calculadora, o programa deve ter um menu de opçoes para realizar os calculos de adiçao, subtração, multiplicaçao e divisão, o programa deve receber 2 números e realizar o cálculo conforme a opção que o usuário selecionar.

def menu():
    print("""
Selecione uma das opções abaixo:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Sair\n""")

def soma(num1, num2):
    return f"\nA soma entre os números {num1} e {num2} é {num1+num2}"

def sub(num1, num2):
    return f"\nA subtração entre os números {num1} e {num2} é {num1-num2}"

def multi(num1, num2):
    return f"\nA multiplicação entre os números {num1} e {num2} é {num1*num2}"

def div(num1, num2):
    return f"\nA divisão entre os números {num1} e {num2} é {num1/num2}"

while True:

    menu()

    op = input("Digite a opção desejada: ")

    if op == "5":
        print("\nVocê decidiu sair da calculadora!")
        break

    if op not in "1234":
        print("\nOpção Inválida!")

    else:
        n1 = int(input("\nDigite o primeiro número: "))

        n2 = int(input("\nDigite o segundo número: "))

        if op == "1":
            print(soma(n1, n2))

        elif op == "2":
            print(sub(n1, n2))

        elif op == "3":
            print(multi(n1, n2))

        elif op == "4":
            if n2 == 0:
                print("\nNão é possivel dividir por zero!")
            else:
                print(div(n1, n2)
