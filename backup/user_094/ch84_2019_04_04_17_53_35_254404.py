def inverte_dicionario(dic):
    newdic = {}
    for k,v in dic.items():
        newdic.setdefault(v, []).append(k)
    return newdic