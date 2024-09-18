# Recebendo valor
print("")
salario = float(input("Digite o seu salario: R$ "))

# Salário bruto
print("")
print("Salario bruto", salario)

# Condições
if(salario < 1693.72):
    print("")
    print("Contribuicao do INSS e de: 8%")
    salarioInss = salario * (8 / 100)
    salarioLiquido = salario - salarioInss
    print("Voce contribuiu para o INSS: R$ ", salarioInss)
    print("Salario liquido: R$ ", salarioLiquido)
elif(salario >= 1693.72) & (salario <= 2822.90):
    print("")
    print("Contribuicao do INSS e de: 9%")
    salarioInss = salario * (9 / 100)
    salarioLiquido = salario - salarioInss
    print("Voce contribuiu para o INSS: R$", salarioInss)
    print("Salario liquido: R$", salarioLiquido)
elif(salario >= 2822.91) & (salario <= 5645.80):
    print("")
    print("Contribuicao do INSS e de: 11%")
    salarioInss = salario * (9 / 100)
    salarioLiquido = salario - salarioInss
    print("Voce contribuiu para o INSS: R$", salarioInss)
    print("Salario liquido: R$ ", salarioLiquido)    
else:
    print("Voce nao e condizente com a tabela do INSS")    