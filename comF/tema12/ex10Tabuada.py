# Recebendo valor
numero = int(input("Digite um número (de 1 a 10): "))

# Laço de repetição
while numero not in range(1, 11):
    numero = int(input("Digite um número (de 1 a 10): "))

# Tabuada
print("")
print(f"A tabuada do {numero}: ")
for i in range(1, 11):
    print(f"\033[33m{numero}\033[m x {i} = \033[33m{numero * i}\033[m")
    i += 1