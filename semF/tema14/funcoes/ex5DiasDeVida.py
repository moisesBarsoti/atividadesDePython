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
print(nome,"você já viveu aproximadamente", diasVida, "dias.")