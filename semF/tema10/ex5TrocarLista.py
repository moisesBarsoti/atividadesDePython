# Lista
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Imprimindo a lista sem a conversão
print("")
print("Sem a conversao: ")
print("Lista A:", a)
print("Lista B:", b)

# Fazendo a conversão
#        i f p                
a, b = b[ ::-1], a[::-1]

# Imprimindo a lista com a conversão
print("")
print("Com a conversao: ")
print("Lista A:", a)
print("Lista B:", b)
print("")