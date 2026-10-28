# Verificando o formato de um CPF
import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# if re.fullmatch(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}", cpf):
if re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF não está no formato correto.")