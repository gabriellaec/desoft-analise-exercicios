def inverte_dicionario(dicionario):
    inversão = {}
    for n, v in dicionario.items():
        if not i in inversão:
            inversão[v] = n
        else:
            inversão[n].append(v)
    
    return(inversão)  
