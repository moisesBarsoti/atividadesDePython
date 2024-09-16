# Utilizado para manipular e procurar expressões regulares
import re

# Recebendo Valor
entrada = input("Digite algo (ou deixe em branco): ")

# Expressão regular 
expressaoRegular = r'^$'

# Verificação para ver se corresponde com a entrada
correspondencia = re.match(expressaoRegular, entrada)

# Laço de repetição
while not correspondencia:
    print(f"\033[31mO campo não está vazio\033[m")
    print(f"\033[33mTente novamente: \033[m")
    entrada = input("Digite algo (ou deixe em branco): ")
    correspondencia = re.match(expressaoRegular, entrada)
print(f"\033[36mCampo vazio\033[m")