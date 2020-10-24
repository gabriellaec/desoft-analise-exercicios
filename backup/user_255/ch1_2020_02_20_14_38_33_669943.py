#Função calcula_valor_devido
#Valor Emprestado=1000
#Meses=5
#Juros Comppostos=1%
ve=1000
jc=1/100
m=5
def f(x,y,z):
    vd=ve*(1+jc)**m
    return vd
vd=f(ve,jc,m)
print(vd)