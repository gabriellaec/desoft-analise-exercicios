def zera_negativos(l):
    i = 0
    while i<len(l)+1:
        if l[i]<0:
            l[i] = 0
            i += 1
            