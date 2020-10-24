def inverte_lista (lista):
    i = len(lista)
    lista2 = []
    while i <= len(lista-1):
        lista2.append(lista[i])
        i -= 1
    return lista2