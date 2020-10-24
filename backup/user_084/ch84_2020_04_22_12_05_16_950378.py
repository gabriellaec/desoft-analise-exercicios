def inverte_dicionario(i):
    f=[]
    for c,v in i.items():
        if v in f.keys():
            f[v].append(c)
        f[v]=c
    return f
    