def inverte_lista(lista1):
    lista2 = [0]*len(lista1)
    for i in range(len(lista1)):
        lista2[i] = lista1[len(lista1)-i-1]
    return lista2