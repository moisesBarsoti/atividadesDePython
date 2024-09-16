# Utilizado para manipular e procurar expressões regulares
import re

# Recebendo valor
rg = input("Digite seu RG: ")

# Expressão regular
expressaoRegular = r'^\d{2}\.\d{3}\.\d{3}-\d{1}$'

# Verificação para ver se corresponde com o RG
correspondencia = re.match(expressaoRegular, rg)

# Laço de repetição
while not correspondencia:
    print(f"\033[31mRG inválido\033[m")
    print(f"\033[33mTente colocar novamente: \033[m")
    rg = input("Digite o seu RG: ")
    correspondencia = re.match(expressaoRegular, rg)
print(f"\033[36mRG válido\033[m")