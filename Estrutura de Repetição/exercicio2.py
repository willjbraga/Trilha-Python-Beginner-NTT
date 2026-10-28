# O que é um loop infinito?

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1

# O problema do código anterior era a falta de incrementar o contador, isso gera um loop infinito pois o contador sempre ia ser igual a 0