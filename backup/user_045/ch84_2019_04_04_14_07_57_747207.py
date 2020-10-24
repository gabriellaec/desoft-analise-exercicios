def inverte_dicionario(n):
    d={}
    for k,v in n.items():
        d[v]=[]
       
        d[v].append(k)
    return d
       
            
    