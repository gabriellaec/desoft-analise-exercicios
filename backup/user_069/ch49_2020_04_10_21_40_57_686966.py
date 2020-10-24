def inverte_lista (lista):
    lista_rev = []
    i = len(lista)
    while i > 0:
        lista_rev.append(lista[i])
        i -= 1
    return lista_rev