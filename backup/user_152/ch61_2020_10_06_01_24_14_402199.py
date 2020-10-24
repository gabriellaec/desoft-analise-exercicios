def filtra_positivos(lista):
    size = len(lista)
    par = []
    i = 0
    if size > 0:
        while i<size:
            if lista[i]%2 == 0:
                par.append(lista[i])
            i += 1
    return par