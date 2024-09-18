# Recebendo valores
numeroINteiro = int(input("Digite um numero inteiro: "))
total = 0

# Verificando se o numero e primo
for i in range(1, numeroINteiro + 1):
    if(numeroINteiro % i == 0):
        total += 1
    print(i)

print("numero", numeroINteiro, "foi divisivel", total, "vezes")        

if total == 2:
    print("O numero e primo")
else:
    print("O numero nao e primo")    