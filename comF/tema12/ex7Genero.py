# Recebendo valor
genero = input("Digite às iniciais do seu gênero (M ou F): ").upper()

# Laço de repetição
while genero not in ['M', 'F']:
    print("")
    genero = input("Digite às iniciais do seu gênero (M ou F): ").upper() 

# Imprimindo
if genero == 'M':
    print(f"Você é \033[36mmasculino\033[m")
else:    
    print(f"Você é \033[31mfeminino\033[m")