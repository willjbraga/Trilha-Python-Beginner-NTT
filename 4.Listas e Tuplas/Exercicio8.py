# Removendo o último item de um pedido

pedidos = input("Pedidos feitos (separados por vírgula): ").split(", ")

pedidos.pop()

print(f"Pedidos finais: {pedidos}")