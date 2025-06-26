#Calculadora de IMC
def calcular_imc():
    kg = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = kg / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
# Inicia o programa
calcular_imc()
