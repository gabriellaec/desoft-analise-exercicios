def filtra_positivos(x):
    lista = []
    for i in range(0, len(x)):
        if x[i] == abs(x[i]):
            lista.append(x[i])
    return lista
    