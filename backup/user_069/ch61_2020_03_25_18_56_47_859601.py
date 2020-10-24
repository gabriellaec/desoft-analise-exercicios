def filtra_positivos (numeros_reais):
    i = 0
    numeros_positivos = []
    while i < len(numeros_reais):
        if numeros_reais[i] > 0:
            numeros_positivos.append(numeros_reais[i])
        i += 1
    return (numeros_positivos)