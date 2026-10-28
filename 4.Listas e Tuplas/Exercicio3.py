# Registrando voluntários para uma campanha

voluntarios = []

while True:
    voluntario = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    
    if voluntario == "sair":
        break
    
    voluntarios.append(voluntario)

print(f"Voluntários registrados: {voluntarios}")