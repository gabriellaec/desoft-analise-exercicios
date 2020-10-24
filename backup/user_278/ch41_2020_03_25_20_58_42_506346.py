valores=[-1,-3,5,8,-13,-17]
def zera_negativos(valores):
    i=0
    while i<len(valores):
        if valores[i]<0:
            valores[i]=0
        else:
            valores[i]=valores[i]
        i+=1