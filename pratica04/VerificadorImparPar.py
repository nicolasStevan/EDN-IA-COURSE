#Programa que verifica se o numero e impar ou par e contabilizando quantos numeros foram digitados
def VerificadorImparPar():
    print("Bem-vindo ao Verificador de Números Ímpares e Pares!")
    contador = 0
    numeros = []

    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")

        if entrada.lower() == 'sair':
            break

        try:
            numero = int(entrada)
            numeros.append(numero)
            contador += 1

            if numero % 2 == 0:
                print(f"{numero} é Par.")
            else:
                print(f"{numero} é Ímpar.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print(f"Números digitados: {numeros}")
    print(f"Total de números digitados: {contador}")
# Chamada da função para executar o programa
VerificadorImparPar()