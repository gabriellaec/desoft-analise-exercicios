def inverte_lista(lista):
    lista2 = []
    i = len(lista) - 1
    while i >= 0:
        lista2.append(lista[i])
        i -= 1
    return lista2