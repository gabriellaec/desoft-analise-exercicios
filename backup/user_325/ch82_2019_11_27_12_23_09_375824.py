def primeiras_ocorrencias(x):
    pal = {}
    e = 0
    for i in x:
        if i not in pal:
            pal[i] = e
        e += 1
    return pal