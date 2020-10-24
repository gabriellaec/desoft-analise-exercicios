#valor_emprestado#
#numero_de_parcelas#
#taxa_de_juros#
def calcula_valor_devido(a, x, r):
    x>1
    c=a *(1+r)**x
    return c