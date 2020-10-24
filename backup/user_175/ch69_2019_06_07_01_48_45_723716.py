def junta_listas(x):
    lista = []
    i1 = 0
    while i1 < len(x):
        i2 = 0
        while i2 < len(x[i1]):
            y = x[i1][i2]
            lista.append(y)
            i2 += 1
        i1 += 1
    return lista