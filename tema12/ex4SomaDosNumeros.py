# Recebendo valores
numerosLista = []
i = 1
while i <= 10:
    numeros = int(input(f"Digite o {i} numero: "))
    numerosLista.append(numeros)
    i += 1

# Imprimindo valores
print("")
print("Lista de valores:")
print(f"\033[33m{numerosLista}\033[m")
print("")
print(f"Soma dos valores: \033[36m{sum(numerosLista)}\033[m")