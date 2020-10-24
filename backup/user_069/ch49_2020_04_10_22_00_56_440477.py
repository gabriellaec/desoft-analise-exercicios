def inverte_lista (lista):
    lista_rev = []
    l = len(lista)
    i = -1
    while l > 0:
        lista_rev.append(lista[i])
        i -= 1
        l -= 1
    return lista_rev