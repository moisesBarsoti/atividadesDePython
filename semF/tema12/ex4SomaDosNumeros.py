# Recebendo valores
numerosLista = []
i = 1
while i <= 10:
    numeros = int(input("Digite o numero: "))
    numerosLista.append(numeros)
    i += 1

# Imprimindo valores
print("")
print("Lista de valores:")
print(numerosLista)
print("")
print("Soma dos valores:", sum(numerosLista))