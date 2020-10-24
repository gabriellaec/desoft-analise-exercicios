"""
OBS: Prestar atenção na tx de juros, e no período, que devem estar na msm dimensão
"""

def calcula_valor_devido(principal, meses, juros):
    vf = principal * ((1 + juros/100) ** meses)
    return vf

print(calcula_valor_devido(1000, 10, 12))
