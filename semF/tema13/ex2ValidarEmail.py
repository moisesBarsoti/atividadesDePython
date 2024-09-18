# Recebendo valor
email = input("Crie o seu e-mail: ")
print("Criado com sucesso!")
print("")

validandoEmail = input("Digite o seu e-mail: ")

# Condição
if email == validandoEmail:
    print("E-mail válido")
else:
    print("E-mail inválido")