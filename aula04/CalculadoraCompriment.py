#fazer uma calculadora de comprimentos, altura, largura, perímetro e área de um retângulo, que o usuário insira os dados e trate com exceção
def calcular_volume_comprimento(comprimento,largura,altura):
  return comprimento * largura * altura

volume = calcular_volume_comprimento(5, 3, 2)
print(f"O volume do retângulo é: {volume} unidades cúbicas")
