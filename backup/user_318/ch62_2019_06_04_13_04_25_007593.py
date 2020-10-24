def filtra_positivos(x):
    positivos=[]
    for i in x:
        if i > 0:
            positivos.append(x)
        else:
            positivos.append(0)
    return [positivos]
