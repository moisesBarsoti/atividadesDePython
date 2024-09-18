# Utilizado para manipular e procurar expressões regulares
import re

# Recebendo valor
hora = input("Digite a hora (00:00:00): ")

# Expressão regular
expressaoRegular = r'^\d{2}:\d{2}:\d{2}$'

# Verificação para ver se corresponde com a hora
correspondencia = re.match(expressaoRegular, hora)

# Laço de repetição
while not correspondencia:
    print(f"\033[31mHora inválida\033[m")
    print(f"\033[33mTente colocar novamente: \033[m")
    hora = input("Digite a hora (00:00:00): ")
    correspondencia = re.match(expressaoRegular, hora)
print(f"\033[36mHora válida\033[m")