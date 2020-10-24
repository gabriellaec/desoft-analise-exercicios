def calcula_valor_devido(v,n,i)
    m=v*(1+i)**n
    return m
v=3000
n=6
i=1/10
print (calcula_valor_devido(v,n,i))