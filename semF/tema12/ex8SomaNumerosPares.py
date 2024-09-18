# Valores
numeros = [1,100]

# Inicializador de soma
soma = 0

# Laço de repetição
for i in range(numeros[0],numeros[1] + 1):
    if i % 2 == 0:
        print(i, "número par")
        soma += i
        print("Resultado:", soma)
    else:
        print(i, "numero impar")

print("")
print("Resulatdo final da soma dos pares:", soma)
print("")