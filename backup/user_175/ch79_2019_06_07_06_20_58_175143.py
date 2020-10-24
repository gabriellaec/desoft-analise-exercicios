def monta_dicionario(x,y):
    dicionario_montado = {}
    for i in x:
        dicionario_montado[i] = y[x.index(i)]
    return dicionario_montado
