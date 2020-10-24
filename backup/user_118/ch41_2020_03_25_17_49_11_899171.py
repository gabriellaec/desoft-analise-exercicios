def zera_negativos(valores):
    valores=0
    i=0
    while i<len(valores):
        if valores[i]<0:
            valores[i]=0
        i+=1
    return valores