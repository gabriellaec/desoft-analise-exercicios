a = [-2, 4, 0, 24, -31, -1]
def zera_negativos(lista):
    i = 0
    if lista[i] < 0:
        lista[i] = 0
    else:
        lista[i] = lista[i]
    i += 1
    return lista
    print(zera_negativos(a))