# Aprovando empréstimo

renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

if (renda > 2000.0) and ((parcela/renda) <= 0.3):
    print("Emprestimo aprovado!")
else:
    print("Empréstimo negado: parcela acima de 30% da renda")