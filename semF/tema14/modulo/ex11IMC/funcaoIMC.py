# Recebendo valores
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# Laço de repetição
while (peso == 0) | (altura == 0):
    print("")
    print("Os dois valores precisam ser maiores que 0")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

# Conta
imc = peso / (altura * altura)
print(imc)

# Condição
if imc <= 16.9:
    print("")
    print("Muito abaixo do peso:")
    print("")
    print("O seu peso é:", peso)
    print("A sua altura é:", altura)
    print("O seu IMC é:", imc)
elif (imc >= 17) and (imc <= 18.4):
    print("")
    print("Abaixo do peso: ")
    print("")
    print("O seu peso é:", peso)
    print("A sua altura é:", altura)
    print("O seu IMC é:", imc)
elif (imc >= 18.5) and (imc <= 24.9):
    print("")
    print("Peso normal: ")
    print("")
    print("O seu peso é:", peso)
    print("A sua altura é:", altura)
    print("O seu IMC é:", imc)
elif (imc >= 25) and (imc <= 29.9):
    print("")
    print("Acima do peso: ")
    print("")
    print("O seu peso é: ", peso)
    print("A sua altura é:", altura)
    print("O seu IMC é:", imc)
elif (imc >= 30) and (imc <= 34.9):
    print("")
    print("Obesidade grau I: ")
    print("")
    print("O seu peso é:", peso)
    print("A sua altura é:", altura)
    print("O seu IMC é:", imc)
elif (imc >= 35) and (imc < 40):
    print("")
    print("Obesidade grau II: ")
    print("")
    print("O seu peso é:", peso)
    print("A sua altura é:", altura)
    print("O seu IMC é:", imc)
else:
    print("")
    print("Obesidade grau III: ")
    print("")
    print("O seu peso é:", peso)
    print("A sua altura é:", altura)
    print("O seu IMC é:", imc)