# Recebendo valor
temperaturaCelsius = int(input("Digite a temperatura da escala Celsius: "))

# Conversão para Fahrenheit
temperaturaFahrenheit = ((temperaturaCelsius * 9) / 5 ) + 32

# Imprimindo
print("")
print(f"\033[33m Celsius: \033[m {temperaturaCelsius}")
print(f"\033[36m Fahrenheit: \033[m {temperaturaFahrenheit}")