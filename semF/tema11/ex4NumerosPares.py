# Lista
print("")
print("Numeros do sistema: ")
numeros = [10,4,2,13,5,67,3]
print(numeros)

# Numero digitado pelo usuario
print("")
numUsuario = int(input("Digite um numero par: "))

# Inicializador da soma
Inicializador = 0

# Laços de repetição
while numUsuario % 2 == 1: 
    numUsuario = int(input("Digite um numero par: "))

for i in numeros:
    if i % 2 == 0:
        print("Numero par do sistema:", i)
        Inicializador += i


# Soma da lista com o numero do usuário
soma = numUsuario + Inicializador

# Iprimindo resultado
print("")
print("Numero do sistema:", Inicializador)
print("Numero do usuario:", numUsuario)
print(Inicializador," + ", numUsuario, " = ", soma)