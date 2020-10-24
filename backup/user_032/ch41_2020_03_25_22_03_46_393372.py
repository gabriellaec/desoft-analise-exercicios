lista_41 = [6,3,-4,0,98,-8,88,-36]
def zera_negativos(lista_41):
    i = 0
    while i < len(lista_41):
        if lista_41[i] < 0:
            lista_41[i] = 0
        i += 1
    return lista_41