def filtra_positivos(x):
    y = []
    i = 0
    while i < len(x):
        if x[i] > 0 :
            y.append(x[i])
            i = i + 1
        else:
            i = i +  1
    return y