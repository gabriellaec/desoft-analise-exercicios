def calcula_valor_devido(principal, meses, juros):
    vf = principal * ((1 + juros) ** meses)
    return vf
