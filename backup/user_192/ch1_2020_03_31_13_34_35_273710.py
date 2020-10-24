def calcula_valor_devido(valor, meses, juros):
    y = valor*(1+juros)**meses
    return y