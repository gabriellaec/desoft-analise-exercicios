def inverte_dicionario(dic):
    newdic = {}
    for k, v in dic.iteritems():
        newdic[v] = newdic.get(v,[])
        newdic[v].append(k)
    return newdic
        