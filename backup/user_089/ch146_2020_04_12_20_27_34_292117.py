def conta_ocorrencias(x):
    d = {}
    i = 0
    for e in x:
        if e not in d:
            d[e] = i
        if e in d:
            d[e] = d[e] + 1
            i = i + 1
    return d