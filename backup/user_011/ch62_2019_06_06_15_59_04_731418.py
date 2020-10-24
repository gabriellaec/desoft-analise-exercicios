def filtra_positivos(numeros):
    listaPositivos = []
    i = 0
    while i < len(numeros):
        if numeros[i] > 0:
            listaPositivos.append(numeros[i])
        i += 1
    return listaPositivos