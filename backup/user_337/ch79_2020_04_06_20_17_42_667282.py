def monta_dicionario (x, y):
    dicionario = {}
    indice = 0
    for i in x:
        dicionario[i] = y[indice]
        indice += 1
    return dicionario