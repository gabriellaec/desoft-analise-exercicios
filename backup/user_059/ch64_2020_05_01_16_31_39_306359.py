def conta_bigramas(x):
    noval = []
    for e in range(len(x)-1):
        noval.append(x[e] + x[e+1])
    return noval