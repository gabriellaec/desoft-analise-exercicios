
def filtra_positivos(lista):
    pos = []
    i = 0
    while i<len(lista):
        if lista[i]>0:
            pos.append(lista[i])
            i += 1
        else:
            i += 1
    else:
        return pos