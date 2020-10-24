def calcula_valor_devido(valor0,juros,n):
    y = valor0*(1+juros)**n
    return y

valor0=100
juros=0.02
n=6
print(calcula_valor_devido(valor0,juros,n))
