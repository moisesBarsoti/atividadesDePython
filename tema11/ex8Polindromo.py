# Recebendo valor
numero = int(input("Digite um número inteiro: "))

# Convertendo o número para string e invertendo
numeroParaStr = str(numero)
numeroInvertido = numeroParaStr[::-1]

# Verificando se é palíndromo
print("")
if numeroParaStr == numeroInvertido:
    print(f"\033[33m{numero}\033[m é um palíndromo.")
else:
    print(f"\033[33m{numero}\033[m não é um palíndromo.")
