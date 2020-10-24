def inverte_dicionario(dic):
    dictinv = {}
    for k in dic.values():
        dictinv[k] = []
    for v,k in dic.items():
        dictinv[k].append(v)
    return dictinv