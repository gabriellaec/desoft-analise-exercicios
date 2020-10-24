def acha_bigramas(x):
    l = []
    for e in range(len(x)-1):
        l.append(x[e] + x[e+1])
    noval = []
    for i in range(len(l)):
        if l[i] not in noval:
            noval.append(l[i])
    return noval
