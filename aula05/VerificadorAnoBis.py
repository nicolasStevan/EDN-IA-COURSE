#Programa que verifica se um ano é bissexto ou não (divisível por 4, exceto se for divisível por 100, a menos que seja divisível por 400)
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
# Fim do programa