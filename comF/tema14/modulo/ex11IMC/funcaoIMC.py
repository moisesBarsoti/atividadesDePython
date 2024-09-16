def calculandoIMC():
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
        print(f"\033[1;47mMuito abaixo do peso:\033[m")
        print("")
        print(f"O seu \033[33mpeso\033[m é: \033[33m{peso}\033[m")
        print(f"A sua \033[36maltura\033[m é: \033[36m{altura}\033[m")
        print(f"O seu \033[35mIMC\033[m é: \033[35m{imc:.2f}\033[m")
    elif (imc >= 17) and (imc <= 18.4):
        print("")
        print("Abaixo do peso: ")
        print("")
        print(f"O seu \033[33mpeso\033[m é: \033[33m{peso}\033[m")
        print(f"A sua \033[36maltura\033[m é: \033[36m{altura}\033[m")
        print(f"O seu \033[35mIMC\033[m é: \033[35m{imc:.2f}\033[m")
    elif (imc >= 18.5) and (imc <= 24.9):
        print("")
        print("Peso normal: ")
        print("")
        print(f"O seu \033[33mpeso\033[m é: \033[33m{peso}\033[m")
        print(f"A sua \033[36maltura\033[m é: \033[36m{altura}\033[m")
        print(f"O seu \033[35mIMC\033[m é: \033[35m{imc:.2f}\033[m")
    elif (imc >= 25) and (imc <= 29.9):
        print("")
        print("Acima do peso: ")
        print("")
        print(f"O seu \033[33mpeso\033[m é: \033[33m{peso}\033[m")
        print(f"A sua \033[36maltura\033[m é: \033[36m{altura}\033[m")
        print(f"O seu \033[35mIMC\033[m é: \033[35m{imc:.2f}\033[m")
    elif (imc >= 30) and (imc <= 34.9):
        print("")
        print("Obesidade grau I: ")
        print("")
        print(f"O seu \033[33mpeso\033[m é: \033[33m{peso}\033[m")
        print(f"A sua \033[36maltura\033[m é: \033[36m{altura}\033[m")
        print(f"O seu \033[35mIMC\033[m é: \033[35m{imc:.2f}\033[m")
    elif (imc >= 35) and (imc < 40):
        print("")
        print("Obesidade grau II: ")
        print("")
        print(f"O seu \033[33mpeso\033[m é: \033[33m{peso}\033[m")
        print(f"A sua \033[36maltura\033[m é: \033[36m{altura}\033[m")
        print(f"O seu \033[35mIMC\033[m é: \033[35m{imc:.2f}\033[m")
    else:
        print("")
        print("Obesidade grau III: ")
        print("")
        print(f"O seu \033[33mpeso\033[m é: \033[33m{peso}\033[m")
        print(f"A sua \033[36maltura\033[m é: \033[36m{altura}\033[m")
        print(f"O seu \033[35mIMC\033[m é: \033[35m{imc:.2f}\033[m")