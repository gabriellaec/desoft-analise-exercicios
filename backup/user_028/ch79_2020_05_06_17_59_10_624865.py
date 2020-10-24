def monta_dicionario(x,y):
    dicionario = {}
    for i in x:
        chaves = x[i]
    for e in y:
        valores = y[i]
    for chave in dicionario.keys():
        for valor in dicionario.values():
            dicionario[chaves] = valores
    return dicionario