def monta_dicionario(x,y):
    aaa = dict()
    c = 0
    while c < len(x):
        aaa[x[c]] = y[c]
        c += 1
    return aaa
        