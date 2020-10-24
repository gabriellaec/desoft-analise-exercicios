def interseccao_chaves(x, y):
    z = list()
    for k in x.keys():
        z.append(k)
    for c in y.keys():
        z.append(c)
    return z
        