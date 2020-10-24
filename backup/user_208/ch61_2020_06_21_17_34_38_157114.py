def filtra_positivos (lista):
    i = 0
    lista1 =[]
    while i <len(lista):
        if lista[i] > 0:
            lista1.append(lista[i])
        i+=1
    return lista1