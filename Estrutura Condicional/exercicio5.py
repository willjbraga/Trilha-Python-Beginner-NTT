# Controlando o orçamento mensal

despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > 3000.0:
    print("Atenção! Você ultrapassou o limite do orçamento")
else:
    print("Você ainda esta dentro do orçamento")