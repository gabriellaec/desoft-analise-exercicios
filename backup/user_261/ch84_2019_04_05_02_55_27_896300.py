def inverte_dicionario(dicionario):
    d={}
    for nome, idade in dicionario.items():
        if idade not in d:
            d[idade]=nome
        else:
            d[idade]+=nome
    
    return d
            
