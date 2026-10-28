# Monitorando vendas no comércio

macas = int(input("Digite a quantidade de maçãs vendidas: "))
bananas = int(input("Digite a quantidade de bananas vendidas: "))

if macas > bananas:
    print("\nMais maçãs foram vendidas.")
elif bananas > macas:
    print("\nMais bananas foram vendidas.")
else:
    print("\nA quantidade de maçãs e bananas vendidas é igual.")

