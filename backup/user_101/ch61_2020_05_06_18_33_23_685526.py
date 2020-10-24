def filtra_positivos(lista):
    posit = []
    for e in lista:
        if e > 0:
            posit.append(e)
    return posit