def calcula_valor_devido(valor, meses, taxa):
    y= valor*(1+taxa/100)**meses
    return y
