def filtra_positivos (numeros):
    lista = []
    i = 0
    while i < len(numeros):
        if numeros[i] > 0:
            lista.append(numeros[i])
            i = i + 1
    return lista