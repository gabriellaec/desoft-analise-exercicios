def calcular_valor_devido(c,x,n):
    m = c*(1+n)**x
    return m
c=1000
x=7
n=0.4
print(calcular_valor_devido(c,x,n))