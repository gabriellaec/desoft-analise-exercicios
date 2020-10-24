def primeiras_ocorrencias(x):
    pal = {}
    e = 0
    for i in x:
        pal[i] = e
        e += 1
    return pal
