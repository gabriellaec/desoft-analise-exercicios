def zera_negativos(l):
    i = 0
    while i < len(l):
        if l[i] < 0:
            l[i] = 0
            i += 1
        else:
            i += 1
    return l