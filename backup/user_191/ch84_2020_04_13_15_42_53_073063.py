def inverte_dicionario(n):
    t=list(n.keys())
    y=list(n.values())
    dic={}
    for i in range(len(t)):
        dic[y[i]]=t[i]
    return dic