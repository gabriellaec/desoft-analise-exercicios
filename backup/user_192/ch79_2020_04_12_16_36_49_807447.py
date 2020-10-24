def monta_dicionario(x, y):
    d = dict()
    for i in len(x):
        for j in len(y):
            d[x[i]] = y[i]
    return d
        