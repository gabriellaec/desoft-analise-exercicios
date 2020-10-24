valor_emprestado = int(input('valor emprestado= '))
numero_de_meses = int(input('numero de meses= '))
taxa_de_juros = int(input('taxa de juros= '))

def calcula_valor_devido(montante):
    montante = valor_emprestado * (1 + taxa_de_juros / 100) ** numero_de_meses
    
    return montante
montante = calcula_valor_devido(valor_emprestado)
print(montante)
