def inverte_dicionario(dic):
    dic2 = {}
    for k,v in dic:
        dic[v] = k
    return dic2