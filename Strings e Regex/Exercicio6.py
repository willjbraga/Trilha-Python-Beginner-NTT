# Substituindo palavras específicas
import re

texto = input("Digite o texto a ser revisado: ")
palavra = input("palavra deseja substituir? ")
nova = input("Qual a nova palavra? ")

print(f"{re.sub(palavra, nova, texto)}")
