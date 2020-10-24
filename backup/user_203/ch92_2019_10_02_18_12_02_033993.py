def simplifica_dict(dicionario): 
    lista = [] 
    for k, v in dicionario.items():
        if k != v and k in dicionario.items():
            lista.append(k) 
        if v == v and v in dicionario.items():
            lista.append(v) 