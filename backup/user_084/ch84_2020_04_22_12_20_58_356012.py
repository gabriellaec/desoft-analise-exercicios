def inverte_dicionario(i):
    f={}
    for c,v in i.items():
        if v not in f.keys():
            f[v]=[]
        
        f[v].append(c)
    return f
    