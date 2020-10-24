def interseccao_chaves(x, y):
    z = list()
    for k in x.keys():
        for c in y.keys():
            if k == c:
                z.append(k)
    return z
        