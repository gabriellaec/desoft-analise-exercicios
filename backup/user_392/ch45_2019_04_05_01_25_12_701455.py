def zera_negativos(lista):
    lista1 = []
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            lista [i] = 0
            lista1.append lista[1]
        else:
            lista1.append lista[i]
     return lista1
        