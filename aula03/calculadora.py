#CALCULADORA DE ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO QUE O USUÁRIO INSIRA OS DADOS SE FOR FLOAT TRATE COM EXCEÇÃO
def calcular():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos.")
        return

    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        return

    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
if __name__ == "__main__":
    calcular()


