#Programa que verifica se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente ignorando espaços e acentos) dizendo se é verdadeiro ou falso
def VerificPalindromo(palavra):
    # Remove espaços e converte para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Remove acentos
    acentos = str.maketrans("áéíóúãõç", "aeiouaoc")
    palavra = palavra.translate(acentos)
    
    # Verifica se a palavra é igual à sua reversa
    return palavra == palavra[::-1]
# Chamada da função para executar o programa
palavra = input("Digite uma palavra ou frase: ")
if VerificPalindromo(palavra):
    print("A palavra ou frase é um palíndromo.")
else:
    print("A palavra ou frase não é um palíndromo.")

