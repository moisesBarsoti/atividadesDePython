# Recebendo valores
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

def diasDeVida(nome, idade):
    nome = nome
    diasDeVida = idade * 365
    return diasDeVida

# instanciando
diasVida = diasDeVida(nome, idade)

# Imprimndo
print("")
print(f"\033[33m{nome}\033[m, você já viveu aproximadamente \033[33m{diasVida}\033[m dias.")