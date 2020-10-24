def calcula_valor_devido(valoremp, meses, taxa):
    x=(valoremp*((1+(taxa/100))**meses))
    return x
