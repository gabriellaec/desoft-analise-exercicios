def conta_bigramas(x):
    dicionario = {}
    for i in range(len(x)-1):
        dicionario[x[i],x[i+1]] = 0
    for i in range(len(x)-1):
        dicionario[x[i],x[i+1]] += 1
    return dicionario