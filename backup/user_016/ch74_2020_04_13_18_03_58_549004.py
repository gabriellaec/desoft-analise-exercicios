def conta_bigramas(x):
    lista = []
    for i in range(0,len(lista)-1):
        lista.append(x[i] + x[i+1])
    dicionario = {}
    for u in lista:
        if u not in dicionario.keys():
            dicionario[u] = 1
        else:
            dicionario[u] = +1
    return dicionario
    
    