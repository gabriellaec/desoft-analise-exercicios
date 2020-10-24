def conta_bigramas(x):
    dicionario = {}
    lista = []
    for t in range(0, len(x)-1):
        lista.append(x[t]+x[t+1])
        
    for i in lista:
        if i in dicionario.keys():
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario
    