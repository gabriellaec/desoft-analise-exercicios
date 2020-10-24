def inverte_dicionario(dic):
    k1 = dic.keys()
    v1 = dic.values()
    novo = {}
    for e in v1:
        if e in k1:
            novo[e] = k1
    
    return novo   