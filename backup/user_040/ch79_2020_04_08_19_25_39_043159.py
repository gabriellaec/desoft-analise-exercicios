def monta_dicionario(x,y):
    dicionario = {}
    for z in x:
        dicionario["{0}".format(x[z])] = y[z]
    return dicionario