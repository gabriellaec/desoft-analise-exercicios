def inverte_dicionario(dic):
    dic2 = {}
    for k,v in dic.items():
        dic2[v] = k
        dic2[k] = v
    return dic2