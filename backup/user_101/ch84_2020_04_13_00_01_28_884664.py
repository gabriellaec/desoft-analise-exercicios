def inverte_dicionario(dic):
    dic_i = {}
    for k, v in dic.items():
        dic_i[v] = k
    return dic_i