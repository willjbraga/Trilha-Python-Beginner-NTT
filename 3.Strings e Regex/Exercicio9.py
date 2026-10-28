# Encontrando palavras que começam com uma letra específica
import re

titulo = input("Digite o título do livro: ")
inicial = input("Digite a letra inicial para pesquisa: ")

resultado = re.findall(rf"\b{inicial}[a-z]+", titulo)

print(resultado)