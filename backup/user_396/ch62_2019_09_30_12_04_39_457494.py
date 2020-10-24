def filtra_positivos(x):
    i = 0 
    lis = []
    while i < len(x) - 1:
        if x[i] > 0:
            lis.append(x[i])
        i += 1
        return lis