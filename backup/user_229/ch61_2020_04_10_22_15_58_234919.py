def filtra_positivos(reais):
    positivos = []
    for i in range(len(reais)):
        if reais[i] > 0:
            positivos.append(reais[i])
    return positivos