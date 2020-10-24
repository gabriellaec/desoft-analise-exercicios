def conta_bigramas(x):
    i = 0
    dicionario = {}
    for i in range(len(x)-1):
        bigrama = x[i] + x[i+1]
        if bigrama not in dicionario:
            dicionario[bigrama] = 1 
        else:
            dicionario[bigrama] += 1
    return dicionario