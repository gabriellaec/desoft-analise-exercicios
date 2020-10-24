def inverte_dicionario(dic):
    dictinv = {}
    for v in dic.values():
        dictinv[v] = []
    for k,v in dic.items():
        dictinv[v].append(k)
    return dictinv