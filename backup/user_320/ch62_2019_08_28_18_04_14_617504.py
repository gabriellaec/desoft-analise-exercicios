def filtra_positivos(lista):
    positivos = []
    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
    return positivos