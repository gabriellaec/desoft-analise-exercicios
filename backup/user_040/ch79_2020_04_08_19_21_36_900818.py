def monta_dicionario(x,y):
    dicionario = {}
    for letra in x:
        dicionario[x[letra]] = y[letra]
    return dicionario