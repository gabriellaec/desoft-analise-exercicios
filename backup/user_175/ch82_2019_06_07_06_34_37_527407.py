def primeiras_ocorrencias(x):
    dicionario = {}
    for i in x:
        dicionario[i] = x.index(i)
    return dicionario