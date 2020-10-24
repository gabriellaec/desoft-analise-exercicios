def inverte_dicionario(dic):
    dic_i = {}
    for k, v in dic.items():
        if v not in dic_i:
            dic_i[v] = [k]
        else:
            dic_i[v].append(k)
    return dic_i