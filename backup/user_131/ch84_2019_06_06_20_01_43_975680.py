def inverte_dicionario(dicionario):
    novo_dicio = dict()
    
    for k,v in dicionario.items():
    
        if v not in novo_dicio:
            novo_dicio[v]=[k]
        
        else:
            novo_dicio[v].append(k)
    return novo_dicio