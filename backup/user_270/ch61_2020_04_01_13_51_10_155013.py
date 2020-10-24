def filtra_positivos(l):
    i = 0
    while i < len(l):
        if l[i] < 1 :
            del l[i]
        i += 1
    return l