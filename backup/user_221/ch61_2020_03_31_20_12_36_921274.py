def filtra_positivos(x):
    i = 0
    positivo = []
    while i < len(x):
        if x[i] > 0:
            positivo.append(x[i])
        i = i + 1
    return positivo