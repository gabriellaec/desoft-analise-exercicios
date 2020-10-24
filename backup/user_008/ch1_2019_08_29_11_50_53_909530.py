def calcular_valor_devido(valor, meses, juros):
    vf = valor*(1+juros/100)**meses
    return vf

print(calcular_valor_devido(100,12,1))