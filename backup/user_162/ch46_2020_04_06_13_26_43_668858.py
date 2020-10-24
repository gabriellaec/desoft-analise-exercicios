def numero_no_indice(l):
    nni = []
    for i in l:
        if i == l.index(i):
            nni.append(i)
    return nni