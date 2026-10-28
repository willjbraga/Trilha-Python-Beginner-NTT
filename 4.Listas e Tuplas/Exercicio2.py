# Organizando notas de um concurso de redação

notas = []

escolha = "s"

while escolha == "s":
    nota = float(input("Digite a nota do aluno: "))
    escolha = input("Deseja digitar outra nota? Digite s para sim e n para encerrar: ")
    notas.append(nota)
    
notas.sort()

print(notas)