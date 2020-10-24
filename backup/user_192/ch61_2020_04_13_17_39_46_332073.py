def filtra_positivos(x):
    a=list()
    for i in range(len(x)):
        if x[i] > 0:
            a.append(x[i])
    return a