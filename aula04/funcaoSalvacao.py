#Fazer uma função salvacao que recebe o nome do usuário e retorna uma mensagem de saudação personalizada, tratando exceções caso o nome seja inválido (vazio ou não seja uma string).
def funcao_salvacao(nome):
    return f"Olá, {nome}! Seja bem-vindo!"
nomesalvacao = funcao_salvacao("Nicolas")
print(nomesalvacao)
