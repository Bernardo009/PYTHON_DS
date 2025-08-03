n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"A média é: {media}")

if media >= 7:
    print(f"Com a media {media}: O aluno foi aprovado!")
elif media <= 2:
    print(f"Com a media {media}:O aluno foi reprovado!")
else:
    print(f"Com a media {media}: O aluno está de recuperação!")

rec = float(input("Digite a nota: "))

mediaRec = (media + rec) / 2

print(f"Média de recuperação é: {mediaRec}")

if mediaRec >= 5:
    print("O aluno foi aprovado!")
elif mediaRec < 5:
    print("O aluno foi reprovado!")
else:
    print("O aluno pegou dp")
