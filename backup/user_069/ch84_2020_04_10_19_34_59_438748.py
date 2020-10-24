def inverte_dicionario (dic):
    dic_rev = {}
    for k, v in dic.items():
        dic_rev[v] = k
    return dic_rev