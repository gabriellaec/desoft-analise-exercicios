def calcula_valor_devido(valoremp, meses, juros):
    dev = valoremp*((1+juros)**meses)
    return dev