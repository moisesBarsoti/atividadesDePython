# Recebendo valor
genero = input("Digite às iniciais do seu gênero (M ou F): ").upper()

# Laço de repetição
while genero not in ['M', 'F']:
    print("")
    genero = input("Digite às iniciais do seu gênero (M ou F): ").upper() 

# Imprimindo
if genero == 'M':
    print("Seu gênero é: Masculino")
else:    
    print("Seu gênero é: Feminino")