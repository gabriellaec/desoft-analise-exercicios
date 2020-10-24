def filtra_positivos(lista):
    i = 0
    f = len(lista)
    lista2 = []
    while i < f:
        if lista[i]>0:
            lista2.append(lista[i])
        i+=1
    return lista2
                     