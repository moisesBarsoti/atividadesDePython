# Recebendo valores
numerosPares = []

# Laço de repetição 
while True:
    numero = int(input("Digite um número (digite 0 para calcular): "))
    
    if numero == 0:
        break
    elif numero % 2 == 0:
        numerosPares.append(numero)

# Imprimindo
if numerosPares:
    media = sum(numerosPares) / len(numerosPares)
    print(f"A média dos números pares digitados é: \033[33m{media}\033[m")
else:
    print("Você não digitou nenhum número")