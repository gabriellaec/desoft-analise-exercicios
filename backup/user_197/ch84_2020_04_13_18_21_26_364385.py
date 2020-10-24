def inverte_dicionario(dic):
    dic2={}
    for i in dic.keys():
        dic2.values().append(i)
    for t in dic.values():
        dic2.keys().append(t)
    return dic2