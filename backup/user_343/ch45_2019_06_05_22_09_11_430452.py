def zera_negativos(lista):
    positivo=[]
    i=0
    while i < len(lista):
        if lista[i]<0:
            positivo.append(lista[i]*(-1))
        else:
            positivo.append(lista[i])
        i=1+i
    return positivo   
        