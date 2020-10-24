
def calcula_valor_devido(principal, meses, juros):
    vf = principal * ((1 + juros/100) ** meses)
    return vf

print(f'{calcula_valor_devido(1000, 5, 2):.02f}')
