def calcula_valor_devido (valor, taxa, meses):
    m = valor*(1+taxa)**meses
    return m