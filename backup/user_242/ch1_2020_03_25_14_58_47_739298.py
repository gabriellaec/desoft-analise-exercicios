Capital = 0
taxa = 0
meses = 0
def Soma(Capital,taxa,meses):
    M = Capital*(1+taxa)**meses
    return M
def calcula_valor_devido (M,Capital):
    Juros = M - Capital
    return Juros
        