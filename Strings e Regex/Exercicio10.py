# Agrupando informações dos pacientes
import re

info = input("Digite o nome completo e o ano de nascimento do paciente: ")

nome = re.findall(r"\w+", info)

print(f"Primeiro nome: {nome[0]}")
print(f"Segundo nome: {nome[1]}")

ano_nascimento = re.findall(r"\d+", info)

print(f"Ano de nascimento: {ano_nascimento[0]}")