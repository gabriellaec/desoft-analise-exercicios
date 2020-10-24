def interseccao_chaves(x, y):
    z = list()
    i=0
    for k, v in x.items():
        z[i] = x.keys()
        i+=1
    for c, va in y.items():
        z[i] = x.keys() + y.keys()
        i+=1
    return z
        