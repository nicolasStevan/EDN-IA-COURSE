#Programa que registra notas de alunos e calcula a media da turma
def RegistroNotaAluno():
    print("Bem-vindo ao Registro de Notas dos Alunos!")
    notas = []
    
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou -1 para finalizar): "))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota registrada.")
# Chamada da função para executar o programa
RegistroNotaAluno()