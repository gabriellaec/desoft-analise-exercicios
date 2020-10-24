def zera_negativos (lista):
    novalista = lista
    i=0
    while i < len(lista):
        if novalista[i] < 0:
            novalista[i]=0
        i+=1
    return novalista
        