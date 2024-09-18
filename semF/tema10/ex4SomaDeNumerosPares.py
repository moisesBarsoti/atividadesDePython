# Lista
valores = [10,5,3,2,4,6]
print("Todos os valores:", valores)

# Inicializador 
somaDosPares = 0

# Laço de repetição
for i in valores:
    if(i % 2 == 0):
        print("Valores pares", i)
        somaDosPares += i

# Imprimindo valores
print("Resultado da soma:", somaDosPares)        