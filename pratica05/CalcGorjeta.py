#Programa que calcula a gorjeta com base no valor da conta e na porcentagem da gorjeta desejada 
# parametros valor_conta e porcentagem_gorjeta
def CalcGorjeta(valor_conta, porcentagem_gorjeta):
    try:
        valor_conta = float(valor_conta)
        porcentagem_gorjeta = float(porcentagem_gorjeta)

        if valor_conta < 0 or porcentagem_gorjeta < 0:
            raise ValueError("Valores não podem ser negativos.")

        gorjeta = valor_conta * (porcentagem_gorjeta / 100)
        total = valor_conta + gorjeta

        print(f"Gorjeta: R$ {gorjeta:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores válidos.")
# Chamada da função para executar o programa
valor_conta = input("Digite o valor da conta: ")
porcentagem_gorjeta = input("Digite a porcentagem da gorjeta: ")
CalcGorjeta(valor_conta, porcentagem_gorjeta)