def filtra_positivos(lista):
    for e in lista:
        if e < 0:
            del e
    return lista