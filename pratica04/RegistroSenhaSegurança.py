#Programa que que serve para verificar se uma senha digitada atende a requisitos de segurança deve ter 8 caracteres e um numero
def RegistroSenhaSeguranca():
    print("Bem-vindo ao Registro de Senha de Segurança!")
    
    while True:
        senha = input("Digite uma senha (mínimo 8 caracteres e pelo menos um número): ")
        
        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres. Tente novamente.")
            continue
        
        if not any(char.isdigit() for char in senha):
            print("A senha deve conter pelo menos um número. Tente novamente.")
            continue
        
        print("Senha registrada com sucesso!")
        break
# Chamada da função para executar o programa
RegistroSenhaSeguranca()