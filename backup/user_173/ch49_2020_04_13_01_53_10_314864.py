def inverte_lista(lista1):
    lista2 = []
    i = 0
    a = 1
    while i < len(lista1):
        lista2.append(lista1[(len(lista1)-a)])
        a += 1
        i += 1
    return lista2