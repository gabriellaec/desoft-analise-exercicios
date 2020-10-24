def primeiras_ocorrencias(x):
    pal = {}
    e = 0
    while e < len(x):
        pal[x[e]] = e
        e += 1
    return pal
