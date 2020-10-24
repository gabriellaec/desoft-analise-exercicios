def calcula_valor_devido(valor_dev,meses,juros):
    vt=(valor_dev*(1-juros))**meses
    return vt