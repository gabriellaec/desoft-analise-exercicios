def zera_negativos (lista):
    positivos=[]
    i=0
    while i<len(lista):
        if lista[i]>=0:
            positivos.append(lista[i])
        elif lista[i]<0:
            positivos.append(0)
            i=i+1
    return positivos 
            