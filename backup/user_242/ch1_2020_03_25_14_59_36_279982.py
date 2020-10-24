Capital = 0
taxa = 0
meses = 0
def calcula_valor_devido(Capital,taxa,meses):
    M = Capital*(1+taxa)**meses
    return M
