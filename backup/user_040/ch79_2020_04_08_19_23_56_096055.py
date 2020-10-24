def monta_dicionario(x,y):
    dicionario = {}
    for z in x:
        dicionario[y[z]] = str(y[z])
    return dicionario