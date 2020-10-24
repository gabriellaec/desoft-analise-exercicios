def monta_dicionario(x,y):
    dicionario = {}
    for i in x:
        if i in y:
            dicionario[x[i]] = y [i]
    return dicionario