def interseccao_valores(x, y):
    z = list()
    for v in x.values():
        for v2 in y.values():
            if v == v2:
                z.append(v)
    return z