import math
def calcula_valor_devido (capital,meses,taxa):
    juros = capital*(1 + taxa)**meses - capital
    return juros
print (calcula_valor_devido(12000,5,0.05))

    