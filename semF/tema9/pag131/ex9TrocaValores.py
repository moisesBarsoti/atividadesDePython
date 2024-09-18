# Recebendo valores
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

# Valores sem a inversão
print("")
print("Valores sem a inversao: ")
print("X:", x)
print("Y:", y)

# Invertendo valores
print("")
x, y = y, x
print("Valores invertidos: ")
print("X:", x)
print("Y:", y)
print("")