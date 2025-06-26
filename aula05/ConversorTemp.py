#Programa conversor de temperatura entre celsius fahrenheit e kelvin
def conversor_temp():
    temperatura = float(input("Digite a temperatura: "))
    unidade = input("Digite a unidade (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

    if unidade == "C":
        fahrenheit = (temperatura * 9/5) + 32
        kelvin = temperatura + 273.15
        print(f"Fahrenheit: {fahrenheit:.2f}")
        print(f"Kelvin: {kelvin:.2f}")
    elif unidade == "F":
        celsius = (temperatura - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"Celsius: {celsius:.2f}")
        print(f"Kelvin: {kelvin:.2f}")
    elif unidade == "K":
        celsius = temperatura - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"Celsius: {celsius:.2f}")
        print(f"Fahrenheit: {fahrenheit:.2f}")
    else:
        print("Unidade inválida.")
# Inicia o programa
conversor_temp()