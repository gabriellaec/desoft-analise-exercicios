def filtra_positivos(x):
    lista = []
    i = 0
    while i < len(x):
        if x[i] > 0:
            lista.append(x[i])
        i += 1
    return lista