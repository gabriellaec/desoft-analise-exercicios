def filtra_positivos(lista):
    positivos = []
    for i in lista:
        if lista[i] > -1:
            positivos.append(lista[i])
    return positivos