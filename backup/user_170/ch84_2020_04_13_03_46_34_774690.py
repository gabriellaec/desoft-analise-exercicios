def inverte_dicionario(dic):
    invDic = {}
    for k ,v in dic.items():
        invDic[v] = k
    return invDic