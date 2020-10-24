def inverte_lista(lista1):
    i = 0
    n = len(lista1)
    lista2 = [0]*n
    while i < n:
        lista2[i] = lista1[-i-1]
        i += 1
    return lista2