def junta_listas(lista):
    a = len(lista)
    listo = []
    for i in range(a):
        b = len(lista[i])
        for j in range(b):
            listo.append(lista[i][j])
    return listo
            