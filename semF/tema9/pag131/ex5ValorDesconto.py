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
print("Produto:", produto)
print("Valor: R$", produtoValor)
print("Porcentagem de desconto:", porcentagemDeDesconto,"%")
print("Total: R$", desconto)