#programa para calcular o preço total de um produto
# Dados do produto nome: Cadeira Infantil, Preço unitáraio: 12,40, Quantidade: 3

nomeProduto = "Cadeira Infantil";
precoUnitario = 12.40;
quantidade = 3;
# Calcular o preço total do produto
precoTotal = precoUnitario * quantidade;
print(f"O preço total do produto {nomeProduto} é: R$ {precoTotal:.2f} reais")