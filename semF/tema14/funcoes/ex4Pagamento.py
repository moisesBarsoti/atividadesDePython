# Recebendo valores
horas = float(input("Digite o número de horas trabalhadas: "))
valor = float(input("Digite o valor pago por hora: "))

def pagamento(horasTrabalhadas, valorHora):
    total = horasTrabalhadas * valorHora
    return total

# Instanciando
valorTotal = pagamento(horas, valor)

# Imprimindo
print("")
print("Horas trabalhadas:", horas)
print("Valor a hora: R$", valor)
print("O valor total a ser pago é: R$", valorTotal)