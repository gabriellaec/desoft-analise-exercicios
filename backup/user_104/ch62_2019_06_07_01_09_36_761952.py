def filtra_positivos(numeros):
    i = 0
    t = len(numeros)
    numeros_novos = []
    while i < t:
        if numeros[i] > 0:
            numeros_novos.append(numeros[i])
        i += 1
    return numeros_novos