def monta_dicionario(x,y):
    dicionario = {}
    for z in x:
        dicionario[y[z]] = int(y[z])
    return dicionario