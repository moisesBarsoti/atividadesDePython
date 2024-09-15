# Valores
numerosLista = []

# Laço de repetição
while True:
    numero = int(input("Digite um numero (Digite 0 para calculara média): "))

    if numero == 0:
        break
    numerosLista.append(numero)    

# Imprimindo
if numerosLista: 
    numeroMinimo = min(numerosLista)
    numeroMaximo = max(numerosLista)
    print(f"O número \033[36mmáximo\033[m da lista é: \033[36m{numeroMaximo}\033[m")
    print(f"O número \033[31mmínimo\033[m da lista é: \033[31m{numeroMinimo}\033[m")
else:
    print("Você não digitou nenhum número")