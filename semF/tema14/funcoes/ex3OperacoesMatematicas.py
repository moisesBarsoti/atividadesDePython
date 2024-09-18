# Soma
def soma(n1, n2):
    return n1 + n2
# Subtração
def subtracao(n1, n2):
    return n1 - n2
# Multiplicação
def multiplicacao(n1, n2):
    return n1 * n2
# Divisão
def divisao(n1, n2):
    return n1 / n2

# Instaciando
contaDeSoma = soma(10,10)
contaDeSubtracao = subtracao(10,10)
contaDeMultiplicacao = multiplicacao(10,10)
contaDeDivisao = divisao(10,10)

# Imprimindo
print("")
print("Resultados: ")
print("")
print(f"Soma: \033[33m{contaDeSoma}\033[m")
print(f"Subtração: \033[33m{contaDeSubtracao}\033[m")
print(f"Multiplicação: \033[33m{contaDeMultiplicacao}\033[m")
print(f"Divisão: \033[33m{contaDeDivisao}\033[m")