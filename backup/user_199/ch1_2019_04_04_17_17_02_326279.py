
def calcula_valor_devido(c,i,t):
    m=c*(1+i)**t
    return m

b=(calcula_valor_devido(2000,0.1,2))
print(b)