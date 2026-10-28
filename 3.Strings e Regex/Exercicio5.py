# Encontrando números em um texto
import re

descricao = input("Digite a descrição da receita: ")

print(f"O número da receita  é: {re.findall(r"\d+", descricao)[0]}")