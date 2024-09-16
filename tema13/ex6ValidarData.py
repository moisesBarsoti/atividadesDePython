# Utilizado para manipular e procurar expressões regulares
import re

# Recebendo valor
data = input("Digite a data (00/00/0000): ")

# Expressão regular
expressaoRegular = r'^\d{2}/\d{2}/\d{4}$'

# Verificação para ver se corresponde com a data
correspondencia = re.match(expressaoRegular, data)

# Laço de repetição
while not correspondencia:
    print(f"\033[31mData inválida\033[m")
    print(f"\033[33mTente colocar novamente: \033[m")
    data = input("Digite a data (dd/mm/aaaa): ")
    correspondencia = re.match(expressaoRegular, data)
print(f"\033[36mData válida\033[m")