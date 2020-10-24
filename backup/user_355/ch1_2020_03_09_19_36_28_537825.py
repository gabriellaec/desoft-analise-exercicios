#valor_da_parcela#
a= 1500
#numero_de_parcelas#
#taxa_de_juros#
r= 1.05
def calcula_valor_devido(x, a, r):
    x>1
    c=(a/x)**r
    return c