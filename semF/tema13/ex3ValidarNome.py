# Utilizado para manipular e procurar expressões regulares
import re

# Recebendo valor
nome = input("Digite o seu nome: ")

# Expressão regular 
expressaoRegular = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]{2,}$'

# Verificação para ver se corresponde com o nome
correspondencia = re.match(expressaoRegular, nome)

# Laço de repetição
while not correspondencia:
    print(f"\033[31mNome inválido\033[m")
    print(f"\033[33mTente colocar novamente: \033[m")
    nome = input("Digite o seu nome: ")
    correspondencia = re.match(expressaoRegular, nome)
print(f"\033[36mNome válido\033[m")