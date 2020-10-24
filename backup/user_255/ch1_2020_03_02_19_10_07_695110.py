#Valor Emprestado=1000
#Meses=5
#Juros Comppostos=1%
def calcula_valor_devido(ve,m,jc):
    if m == 0:
        vd = ve
    else:
        vd = ve*(1+jc)**m
    return vd 