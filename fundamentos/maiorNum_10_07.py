# Crie um programa que peça para o usuario digitar 2 números e exiba qual deles é o maior

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 > num2:
    print(f"O {num1} é maior!")
elif num2 > num1:
    print(f"O {num2} é maior!")
else:
    print("Os números são iguais! \nTente outra vez!")

