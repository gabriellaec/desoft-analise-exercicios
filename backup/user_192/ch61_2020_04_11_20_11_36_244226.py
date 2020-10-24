def filtra_positivos(x):
    a=[0]
    for i in range(len(x)):
        if x[i] > 0:
            a.append(x[i])
            break 
    return a