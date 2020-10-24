def inverte_dicionario(dic):
    chaves = list(dic.keys())
    valores = list(dic.values())
    dic_novo = {}
    for i in valores:
        for e in chaves:
            if chaves[e] not in dic_novo:
                dic_novo[valores[i]] = chaves[e]
            else:
                dic_novo[valores[i]] += chaves[e]
    
