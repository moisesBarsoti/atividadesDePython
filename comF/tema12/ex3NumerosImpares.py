# Valores
numeros = [100,200]

# Laço de repetição
for i in range(numeros[0],numeros[1] + 1):
    if(i % 2 == 1):
        print(f"\033[33m{i}\033[m e numero \033[36mimpar\033[m")
    else:
        print(f"\033[33m{i}\033[m e numero \033[31mpar\033[m")
