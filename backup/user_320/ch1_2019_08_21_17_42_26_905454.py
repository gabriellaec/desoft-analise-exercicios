
def calcula_valor_devido(principal, meses, juros):
    vf = principal * ((1 + juros/100) ** meses)
    return vf


