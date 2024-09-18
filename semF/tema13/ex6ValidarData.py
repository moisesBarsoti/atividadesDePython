# Recebendo valor
data = input("Crie a sua data (00/00/0000): ")
print("Criado com sucesso!")
print("")

validandoData = input("Crie a sua data (00/00/0000): ")

# Condição
if data == validandoData:
    print("Data válida")
else:
    print("Data inválida")