# Utilizado para manipular e procurar expressões regulares
import re

# Recebendo valor
cpf = input("Digite seu CPF: ")

# Expressão regular
expressaoRegular = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

# Verificação para ver se corresponde com o cpf
correspondencia = re.match(expressaoRegular, cpf)

# Laço de repetição
while not correspondencia:
    print(f"\033[31mCPF inválido\033[m")
    print(f"\033[33mTente colocar novamente: \033[m")
    cpf = input("Digite o seu cpf: ")
    correspondencia = re.match(expressaoRegular, cpf)
print(f"\033[36mCPF válido\033[m")