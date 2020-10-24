def inverte_dicionario(dic):
    newdic={}
    for v in dic.values():
        for k in dic.keys():
            if dic[k]==v:
                newdic[v]=k
    return newdic
        