def interseccao_chaves(x, y):
    z = list()
    for k in x.keys():
        z.append(k)
    for c, va in y.values():
        z.append(c)
    return z
        