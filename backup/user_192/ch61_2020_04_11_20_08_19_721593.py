def filtra_positivos(x):
    a=[0]
    for i in range(len(x)):
        if not x[i] < 0:
            a.append(x[i])
    return a