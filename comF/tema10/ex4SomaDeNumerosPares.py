# Lista
valores = [10,5,3,2,4,6]
print(f"Todos os valores: {valores}")

# Inicializador 
somaDosPares = 0

# Laço de repetição
for i in valores:
    if(i % 2 == 0):
        print(f"Valores pares {i}")
        somaDosPares += i

# Imprimindo valores
print(f"Resultado da soma: {somaDosPares}")        