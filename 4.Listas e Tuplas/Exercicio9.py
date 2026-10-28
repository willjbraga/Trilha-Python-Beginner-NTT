# Calculando a média de notas

notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")

media = 0.0

for nota in notas:
    media += float(nota)

media = media/(len(notas))

print(f"Média final da turma: {media:.2f}")