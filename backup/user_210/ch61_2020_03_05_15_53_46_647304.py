def filtra_positivos(l):
    lista = []
    for c in l:
        if c >= 0:
            lista.append(c)
    return lista