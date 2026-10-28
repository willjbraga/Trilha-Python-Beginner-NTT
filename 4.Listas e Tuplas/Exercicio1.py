# Verificando itens na despensa

itens = ['arroz', 'feijão', 'óleo']

item = input("Digite o item que você quer verificar: ")

if item in itens:
    print(f"O item {item} já está na lista.")
else:
    print(f"O item {item} precisa ser comprado.")

print(itens)