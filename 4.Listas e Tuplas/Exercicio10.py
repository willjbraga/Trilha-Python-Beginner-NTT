# Registrando dados de alunos

alunos = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")

for i in range(0, len(alunos), 3):
    aluno, idade, nota = alunos[i], int(alunos[i+1]), float(alunos[i+2])
    print(f"Aluno: {aluno}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota:.2f}\n")