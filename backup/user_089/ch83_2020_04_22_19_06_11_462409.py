def medias_por_inicial(dic):
    novo = {}
    n = 1
    for k in dic:
        if k[0] in novo:
            n += 1
            novo[k[0]] += k
            novo[k[0]] = novo[k[0]]/n
        
        if k[0] not in novo:
            novo[k[0]] = k
        
    return novo                