def primeiras_ocorrencias(x):
    l = list(x)
    d = {}
    for i in range(len(l)):
        if l[i] not in d:
            d[l[i]] = i
    return d