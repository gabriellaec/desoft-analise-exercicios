def calcula_valor_devido(c,n,i):
    x = c*(1+i)**n
    return x
print (calcula_valor_devido(1000,0.35,10))