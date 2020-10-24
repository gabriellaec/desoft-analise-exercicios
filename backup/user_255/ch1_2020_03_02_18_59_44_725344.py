#Valor Emprestado=1000
#Meses=5
#Juros Comppostos=1%
ve=1000
jc=1/100
m=5
def calcula_valor_devido(x,y,z):
    if m==0:	
        vd=ve
    else:
        vd=ve*(1+jc)**m
        return vd    
vd=calcula_valor_devido(ve,jc,m)
print(vd)

    