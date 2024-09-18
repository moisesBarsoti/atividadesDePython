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
    print("O número máximo da lista é:", numeroMaximo)
    print("O número mínimo da lista é:", numeroMinimo)
else:
    print("Você não digitou nenhum número")