def zera_negativos(lista):
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            lista[i] = 0
        i += 1
    return lista
print (zera_negativos([0, 1, 4, -9, 8, -6, -4, 5]))