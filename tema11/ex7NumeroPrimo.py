# Recebendo valores
numeroINteiro = int(input("Digite um numero inteiro: "))

# Verificando se o numero e primo
if numeroINteiro <= 1:
    print("NUmero nao e primo")
for i in range(2, int(numeroINteiro**0.5) + 1):
    if numeroINteiro % i == 0:
    print("NUmero nao e primo")
print("Numero e primo")