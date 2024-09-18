from datetime import datetime

# Função para converter data
def converterData(data):
    # Converte a data para um objeto dia/mês/ano
    try:
        dataObj = datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        return None
    
    # Dicionário de mês
    mesesPorExtenso = {
        1: 'janeiro', 
        2: 'fevereiro', 
        3: 'março', 
        4: 'abril',
        5: 'maio', 
        6: 'junho', 
        7: 'julho', 
        8: 'agosto',
        9: 'setembro', 
        10: 'outubro', 
        11: 'novembro', 
        12: 'dezembro'
    }
    
    # Formata a data no novo formato
    dia = dataObj.day
    mes = mesesPorExtenso[dataObj.month]
    ano = dataObj.year
    
    return f"{dia} de {mes} de {ano}"

# Instanciando
data = input("Digite a data (00/00/0000): ")
resultado = converterData(data)

# Imprimindo
if resultado:
    print(f"Data válida: {resultado}")
else:
    print(f"Data inválida: {resultado}")