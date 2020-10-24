def monta_dicionario(x,y):
    dicionario = {}
    for z in x:
        for h in y:
            dicionario[z] = y[h]
    return dicionario