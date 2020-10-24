def inverte_dicionario(n):
    dicionario = {}
    for k,v, in n.items():
        if v not in dicionario:
            dicionario[v] = [k]
        else:
            dicionario[v].append(k)
    return dicionario
            
        

    