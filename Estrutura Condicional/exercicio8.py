# Calculando pedágio

distancia = float(input("Digite a distância percorrida (em km): "))

if distancia > 200:
    print("Valor do pedágio: R$ 30,00")
elif distancia > 100:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 10,00")