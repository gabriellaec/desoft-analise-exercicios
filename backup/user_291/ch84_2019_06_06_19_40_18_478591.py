def inverte_dicionario(dicionario):
    inversão = {}
    for n, v in dicionario.items():
        if not v in inversão:
            inversão[v] = n
        else:
            inversão[v].append(n)
    
    return(inversão)  
