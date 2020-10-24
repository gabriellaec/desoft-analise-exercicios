def inverte_lista(lista1):
    lista2 = []
    i = 0
    a = 1
    while i < len(lista1):
        lista2.append(lista[(len(lista)-a)])
        a += 1
        i += 1
    return lista2