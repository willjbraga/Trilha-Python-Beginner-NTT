# Reorganizando uma lista de convidados

convidados = ['Ana', 'Pedro', 'Carlos']
print(f"Lista atual de convidados: {convidados}")

convidado = input("Digite o nome do novo convidado: ")
pos = int(input("Digite a posição na qual deseja inserir o convidado: "))

convidados.insert(pos-1, convidado)

print(f"Lista atualizada de convidados: {convidados}")