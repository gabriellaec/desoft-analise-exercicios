def calcula_valor_devido(valor, meses, taxa):
    y= valor*(1+taxa/100)**meses
    return y
x= calcula_valor_devido(300,9,2)
print(x)
