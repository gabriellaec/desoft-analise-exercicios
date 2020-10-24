def inverte_dicionario (dic):
    dic_invert = {}
    for k, v in dic.items():
        if v not in dic_invert:
            dic_invert[v] = []
        dic_invert[v].append(k)
    return dic_invert