def conta_bigramas(x):
    l = list(x)
    noval = []
    for e in range(len(l)-1):
        noval.append(l[e] + l[e+1])
    d = {}
    for i in range(len(noval)):
        if noval[i] not in d:
            d[noval[i]] = 1
        else:
            d[noval[i]] +=1
    return d