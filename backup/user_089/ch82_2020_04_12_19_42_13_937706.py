def primeiras_ocorrencias(x):
    d = {}
    for e in x:
        if e in d:
            d[e] = d[e] + 1
        if e not in d:
            d[e] = 1
    return d