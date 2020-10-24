def zera_negativos(lista):
    lista1 = []
    i = 1
    while i < len(lista):
        if lista[i] < 0:
            lista [i] = 0
            lista1.append (lista[i])
        i += 1
    return lista1
        