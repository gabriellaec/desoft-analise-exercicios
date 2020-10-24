def filtra_positivos(numero):
    i = 0
    positivos = []
    while i < len(numero):
        if numero[i] > 0:
            positivos.append(numero[i])
        else:
            pass
        i += 1
    return positivos
    