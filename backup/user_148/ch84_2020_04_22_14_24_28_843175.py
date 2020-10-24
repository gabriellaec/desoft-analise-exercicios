def inverte_dicionario(d):
    d2 = {}
    
    for k, v in d.items():
        d2[v] = k
        
    return d2