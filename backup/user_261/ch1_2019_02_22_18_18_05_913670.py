def calcula_valor_devido (valor, meses, taxa):
    m = valor*(1+taxa)**meses
    return m