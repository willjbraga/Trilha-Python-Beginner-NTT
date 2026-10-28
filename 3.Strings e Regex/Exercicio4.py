# Verificando o início e o fim de uma String

site = input("Digite a URL para validação: ")

if site.startswith("https://") and site.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida")