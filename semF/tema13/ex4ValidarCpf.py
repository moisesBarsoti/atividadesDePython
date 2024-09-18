# Recebendo valor
cpf = input("Coloque o seu CPF: ")
print("Criado com sucesso!")
print("")

validandoCpf = input("Digite o seu CPF: ")

# Condição
if cpf == validandoCpf:
    print("CPF válido")
else:
    print("CPF inválido")