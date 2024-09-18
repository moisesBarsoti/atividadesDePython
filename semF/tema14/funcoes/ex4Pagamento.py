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
print(f"\033[33mHoras\033[m trabalhadas:\033[33m{horas}\033[m")
print(f"\033[33mValor\033[m a hora: R$ \033[33m{valor}\033[m")
print(f"O \033[34mvalor total\033[m a ser pago é: R$ \033[34m{valorTotal:.2f}\033[m")