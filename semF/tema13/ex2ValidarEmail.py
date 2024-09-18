# Utilizado para manipular e procurar expressões regulares
import re

# Recebendo valor
email = input("Digite o seu e-mail: ")

# Expressão regular 
expressaoRegular = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Verificação para ver se corresponde com o email
correspondencia = re.match(expressaoRegular, email)

# Laço de repetição
while not correspondencia:
    print(f"\033[31mE-mail inválido\033[m")
    print(f"\033[33mTente colocar novamente: \033[m")
    email = input("Digite o seu e-mail: ")
    correspondencia = re.match(expressaoRegular, email)
print(f"\033[36mE-mail válido\033[m")