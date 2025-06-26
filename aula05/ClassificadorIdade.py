#Programa que apos o usuário digitar a idade, informa se é criança, adolescente, adulto ou idoso
idade = int(input("Digite a sua idade: "))
if idade < 12:
    print("Você é uma criança")
elif idade < 17:
    print("Você é um adolescente")
elif idade < 60:
    print("Voce é um adulto")
else:
    print("Voce é um idoso")
# Fim do programa