def inverte_dicionario(n):
    d={}
    for k,v in n.items():
        if v not in d:
            d[v]=[]
        d[v].append(k)
    return d
       
            
    