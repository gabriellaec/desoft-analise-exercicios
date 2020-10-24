def calcular_valor_devido(valor, meses, juros):
    vf = valor*(1+juros)**meses
    return vf

