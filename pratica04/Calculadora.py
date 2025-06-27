#Calculadora que tenha as funcionalidades de soma, subtração, multiplicação e divisão.
def Calculadora():
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite o número da operação (1/2/3/4): ")

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                operacao = "Soma"
            elif escolha == '2':
                resultado = num1 - num2
                operacao = "Subtração"
            elif escolha == '3':
                resultado = num1 * num2
                operacao = "Multiplicação"
            elif escolha == '4':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2
                operacao = "Divisão"

            print(f"O resultado da {operacao} é: {resultado}")
            break
        else:
            print("Opção inválida. Tente novamente.")