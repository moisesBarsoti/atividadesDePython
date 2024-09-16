# Recebendo valores
produto = input("Digite o nome do produto: ")
produtoValor = float(input("Digite o valor do produto: R$ "))
porcentagemDeDesconto = int(input("Qual e a porcentagem de desconto: "))

# Desconto
desconto = produtoValor * (porcentagemDeDesconto / 100)

# Imprimindo os valores
print("")
print("Descricao do produto: ")
print("")
print(f"Produto: \033[1;36m {produto}\033[m")
print(f"Valor: \033[1;33m R${produtoValor}\033[m")
print(f"Porcentagem de desconto: \033[1;32m{porcentagemDeDesconto}% \033[m")
print(f"Total: \033[1;35m R${desconto}\033[m ")