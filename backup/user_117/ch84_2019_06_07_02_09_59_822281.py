def inverte_dicionario (dic):
    dic_invert = {}
    for k, v in dic_invert.items():
        if v not in dic:
            dic_invert = []
        dic_invert.append(v)
    return dic_invert