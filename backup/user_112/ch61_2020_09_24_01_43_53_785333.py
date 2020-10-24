def filtra_positivos(n):
    x = len(n)
    i = 0
    lista = []
    while i < x:
        if n[i] > 0:
            lista.append(n[i])
        i = i + 1
    return(lista)