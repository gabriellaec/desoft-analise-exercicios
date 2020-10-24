def inverte_dicionario(dicionario):
    d={}
    l=[]
    for nome, idade in dicionario.items():
        if idade not in d:
            d[idade]=l.append(nome)
        else:
            d[idade]+=l.append(nome)
    
    return d
            
