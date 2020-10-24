pos = []
def filtra_positivos(x):
    for i in range(0,len(x)):
        if x[i]>0:
            pos.append(x[i])
    return pos
    