def filtra_positivos(lista):
    positivos = []
    x = 0
    n = len(lista)
    i = 0
    while i<n:
        x=lista[i]
        if x>0:
            positivos.append(x)
        i=i+1
    return positivos