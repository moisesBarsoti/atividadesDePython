# Recebendo valor
valorConta = int(input("Digite o valor da conta: R$ "))

# Notas
notaDe50 = 50
notaDe10 = 10
moedaDe1 = 1

# Calculando
contaDe50 = valorConta // notaDe50
valorConta %= notaDe50

contaDe10 = valorConta // notaDe10
valorConta %= notaDe10

contaDe1 = valorConta // moedaDe1
valorConta %= moedaDe1

# Imprimindo
print("")
print("Para pagar a conta você precisará de:")
print("Notas de R$ 50:", contaDe50)
print("Notas de R$ 10:", contaDe10)
print("Moeda de R$ 1:", contaDe1)