def lista_caracteres(x):
    l = []
    for i in range(len(x)):
        if x[i] not in l:
            l.append(x[i])
    return l
        