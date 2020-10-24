def interseccao_chaves(x, y):
    z = list()
    i=0
    for k, v in x.items():
        z.append(k)
    for c, va in y.items():
        z.append(c)
    return z
        