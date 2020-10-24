def filtra_positivos(lista):
    par = []
    if len(lista) > 0:
        i = 0
        while i<len(lista):
            if lista[i]> 0:
                par.append(lista[i])
            i += 1
    return par