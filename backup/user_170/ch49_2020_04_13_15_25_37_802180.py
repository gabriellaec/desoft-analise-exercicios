def inverte_lista(lista1):
    lista2 = []
    for i in range(len(lista1)-1):
        lista2.append(lista1[len(lista1)-1-i])
    return lista2
    