def conta_bigramas(x):
    
    dicionario = {}
    for i in range(len(x)-1):
        bigrama = x[i] + x[i]
        if bigrama not in dicionario:
            dicionario[bigrama] = 1 
        else:
            dicionario[bigrama] += 1
    return dicionario