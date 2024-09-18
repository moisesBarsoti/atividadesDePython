# Recebendo valor
numero = int(input("Digite um número inteiro: "))

# Convertendo o número para string e invertendo
numeroParaStr = str(numero)
numeroInvertido = numeroParaStr[::-1]

# Verificando se é palíndromo
print("")
if numeroParaStr == numeroInvertido:
    print(numero, "é um palíndromo.")
else:
    print(numero, "não é um palíndromo.")
