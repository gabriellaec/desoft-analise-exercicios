def calcula_valor_devido(v,t,n):
    m = v * (1+t)**n
    return m
print (calcula_valor_devido(1000,2,5))