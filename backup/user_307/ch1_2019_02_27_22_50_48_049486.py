valor_emprestado=5000
numero_de_meses=12
taxa_de_juros=20/100

def calcula_valor_devido (valor_emprestado, numero_de_meses, taxa_de_juros):
    y = valor_emprestado*(1+taxa_de_juros)**numero_de_meses
    return y
print(calcula_valor_devido (valor_emprestado, numero_de_meses, taxa_de_juros))

