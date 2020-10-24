def numero_no_indice(l):
    nni = []
    for i in range(len(l)):
        if i == l.index(i):
            nni.append(i)
    return nni        