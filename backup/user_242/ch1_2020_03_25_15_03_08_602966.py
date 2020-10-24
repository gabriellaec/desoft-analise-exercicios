Capital = 0
taxa = 0
meses > 0
def calcula_valor_devido(Capital,taxa,meses):
    m = (Capital*((1+taxa)**meses)) + Capital
    return m
