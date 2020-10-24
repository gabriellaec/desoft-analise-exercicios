def monta_dicionario(x,y):
    dicionario = {}
    for z in x:
        n = x[z]
        dicionario["{0}".format(n)] = y[z]
    return dicionario