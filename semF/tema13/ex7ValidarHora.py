# Recebendo valor
hora = input("Crie a sua hora (00:00:00): ")
print("Criado com sucesso!")
print("")

validandoHora = input("Crie a sua hora (00:00:00): ")

# Condição
if hora == validandoHora:
    print("hora válida")
else:
    print("hora inválida")