def filtra_positivos(x):
    lista = []
    for i in range(0, len(x)):
        if x[i] == abs(x[i]) and x[i] != 0:
            lista.append(x[i])
    return lista
    