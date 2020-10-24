def filtra_positivos(lista):
    positivos = []
    for i in lista:
        if i >= 0:
            positivos.append(i)
    return positivos