def inverte_lista(lista):
    i = len(lista)
    lista2 = []
    while i > 0:
        lista2.append(lista[i-1])
        i-=1
    return lista2
