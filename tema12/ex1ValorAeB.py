# Números pares
pares = [(10, 2),(6,2),(15,3)]

# Laço de repetição
for par in pares:
    a, b = par
    i = 0
    while a > b:
        a -= b
        i += 1
    print(f"Para os números \033[33m{par[0]}\033[m e \033[33m{par[1]}\033[m:")
    print(f"Valor final de A: \033[33m{a}\033[m")
    print(f"Valor final de C: \033[33m{i}\033[m\n")