c=float(input('digite o capital incial: '))
i=float(input('digite a taxa de juros: '))
t=float(input('digite o tempo em anos: '))
def calcula_valor_devido(c,i,t):
    m=c*(1+i)**t
    return m

b=(calcula_valor_devido(c,i,t))
print(b)