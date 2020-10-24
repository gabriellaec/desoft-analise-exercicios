def inverte_dicionario(dic):
    invert=dict()
    for k,v in dic.items():
        if v not in invert:
            invert[v]=k
        else:
            invert[v]+=k
    return invert