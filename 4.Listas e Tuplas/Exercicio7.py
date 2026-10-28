# Corrigindo posições na lista de uma corrida de atletismo
nome_incorreto = input("Digite o nome incorreto: ")
nome_certo = input("Digite o nome correto: ")

resultados = ["Ana", "Carlos", "Pedro"]
print("Lista original:", resultados)

if nome_incorreto in resultados:
    posicao = resultados.index(nome_incorreto)
    resultados.remove(nome_incorreto)
    resultados.insert(posicao, nome_certo)
    print(resultados)
else:
    print("Nome não encontrado na lista")
