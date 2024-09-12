# Lista
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Imprimindo a lista sem a conversão
print("Sem a conversao: ")
print(f"Lista A: {a}")
print(f"Lista B: {b}")

# Fazendo a conversão
#        i f p                
a, b = b[ ::-1], a[::-1]

# Imprimindo a lista com a conversão
print("Com a conversao: ")
print(f"Lista A: {a}")
print(f"Lista B: {b}")