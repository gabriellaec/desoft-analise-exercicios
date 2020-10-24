#valor_da_parcela#
a= 1500
#numero_de_parcelas#
#taxa_de_juros#
r= 1.05
def calcula_valor_devido(x, a, r):
    c=(a/x)**r
    
    return c