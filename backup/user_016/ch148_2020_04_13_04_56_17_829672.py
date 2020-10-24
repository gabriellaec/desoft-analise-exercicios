def conta_letras(x):
    dicionario = {}
    for i in range(0,len(x)):
        dicionario[x[i]] = x.count(x[i])
    return dicionario