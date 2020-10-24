def inverte_dicionario(d):
    d2 = {}
    
    for c in d.values():
        d2['c'] = d.keys()
        
    return d2