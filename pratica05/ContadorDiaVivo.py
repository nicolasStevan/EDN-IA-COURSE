#Programa que calcula quantos dias um individuo esta vivo com base na data e dia
from datetime import datetime
def ContadorDiaVivo(data_nascimento):
    try:
        # Converte a string de data para um objeto datetime
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        
        # Obtém a data atual
        data_atual = datetime.now()
        
        # Calcula a diferença entre as duas datas
        dias_vivo = (data_atual - data_nascimento).days
        
        print(f"Você está vivo há {dias_vivo} dias.")
    
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira uma data válida no formato dd/mm/aaaa.")
# Chamada da função para executar o programa
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
ContadorDiaVivo(data_nascimento)
