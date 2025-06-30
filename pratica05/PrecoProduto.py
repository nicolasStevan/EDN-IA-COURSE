# Programa que calcula o preço final de um produto apos aplicar um desconto.
#Parametros calc_desconto e preco_produto
def calc_desconto(preco_produto, desconto):
    try:
        preco_produto = float(preco_produto)
        desconto = float(desconto)

        if preco_produto < 0 or desconto < 0:
            raise ValueError("Valores não podem ser negativos.")

        preco_final = preco_produto * (1 - desconto / 100)

        print(f"Preço final do produto: R$ {preco_final:.2f}")

    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores válidos.")
# Chamada da função para executar o programa
preco_produto = input("Digite o preço do produto: ")
desconto = input("Digite o desconto a ser aplicado (em %): ")
calc_desconto(preco_produto, desconto) 
