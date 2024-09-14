# Recebendo valor
numero = int(input("Digite um numero: "))

# Condição
if(numero % 2 == 0):
    print(f"O numero \033[33m{numero}\033[m e\033[33m par\033[m")
else:
    print(f"O numero \033[33m{numero}\033[m e\033[33m impar\033[m")
