def filtra_positivos(l):
    i = 0
    new_l = []
    while i < len(l):
        if l[i] > 0 :
            new_l.append(l[i])
        i += 1
    return new_l