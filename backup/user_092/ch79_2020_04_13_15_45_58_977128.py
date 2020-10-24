def monta_dicionario(x,y):
    dicionario={}
    for e in range(len(x)):
        dicionario[x[e]] = y[e]
    return dicionario