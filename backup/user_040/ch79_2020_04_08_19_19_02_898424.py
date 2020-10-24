def monta_dicionario(x,y):
    for i in x:
        if i in y:
            dicionario = {}
            dicionario[x[i]] = y [i]
    return dicionario