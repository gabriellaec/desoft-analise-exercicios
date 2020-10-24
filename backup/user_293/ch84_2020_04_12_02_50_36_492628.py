def inverte_dicionario(dic):
    dic_novo = {}
    for e in dic:
        i = dic[e]
        dic_novo[i] = e
    return dic_novo