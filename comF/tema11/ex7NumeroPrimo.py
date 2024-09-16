# Recebendo valores
numeroINteiro = int(input("Digite um numero inteiro: "))
total = 0

# Verificando se o numero e primo
for i in range(1, numeroINteiro + 1):
    if(numeroINteiro % i == 0):
        print("\033[33m", end='')
        total += 1
    else:
        print("\033[31m", end='')
    print("{} ".format(i), end='')
print(f"\n\033[m0 numero {numeroINteiro} foi divisivel {total} vezes", end='')        
if total == 2:
    print(" O numero e primo")
else:
    print(" O numero nao e primo")    