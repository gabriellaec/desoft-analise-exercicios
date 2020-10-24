def filtra_positivo(lista):
    nl=[]
    i=0
    l=len(lista)
    while i<l:
        if lista[i]>0:
            nl.append(lista[i])
        i+=1
    return nl