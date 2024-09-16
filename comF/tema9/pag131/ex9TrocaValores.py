# Recebendo valores
x = float(input("Digite um valor: "))
y = float(input("Digite um segundo valor: "))

# Valores sem a inversão
print("")
print(f"Valores sem a inversao: \033[36m{x} e {y}\033[m")

# Invertendo valores
print("")
x, y = y, x
print(f"Valores invertidos: \033[33m{x} e {y}\033[m")
print("")