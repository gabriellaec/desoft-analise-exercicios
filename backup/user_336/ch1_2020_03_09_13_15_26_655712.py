def calcular_valor_devido(c,i,n):
    m=c*(1+i)**n
    return m
 c=1000
 i=0.2
 n=7
 print(calcular_valor_devido(c,i,n))