
def calcula_valor_devido(c,i,t):
    m=c*(1+i)**t
    return m
c=2000
i=0.1
t=2
b=(calcula_valor_devido(c,i,t))
print(b)