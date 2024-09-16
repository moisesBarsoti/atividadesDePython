# Valores
numeros = [1,100]

soma = 0

# Laço de repetição
for i in range(numeros[0],numeros[1] + 1):
    if i % 2 == 0:
        print(f"\033[36m{i}\033[m numero \033[36mpar\033[m")
        soma += i
        print(f"Resultado: {soma}")
    else:
        print(f"\033[31m{i}\033[m numero \033[31mimpar\033[m")

print("")
print(f"Resulatdo final da soma dos pares: \033[33m{soma}\033[m")