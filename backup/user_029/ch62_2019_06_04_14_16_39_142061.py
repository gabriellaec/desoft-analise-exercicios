def filtra_positivos(f):
    i = 0 
    positivos = []
    while i < len(f):
        if f[i] > 0:
            positivos.append(f[i])
        i += 1
    return positivos
