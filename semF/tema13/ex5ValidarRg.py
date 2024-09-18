# Recebendo valor
rg = input("Coloque o seu RG: ")
print("Criado com sucesso!")
print("")

validandoRg = input("Digite o seu RG: ")

# Condição
if rg == validandoRg:
    print("RG válido")
else:
    print("RG inválido")