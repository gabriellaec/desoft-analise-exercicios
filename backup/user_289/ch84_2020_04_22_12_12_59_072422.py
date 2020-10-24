def inverte_dicionario(dicionario):
    new_dict = {}
    for k, v in dicionario.items():
        if v not in new_dict.keys():
            lista = []
            lista.append(k)
            new_dict[v] = lista
        else:
            lista = new_dict[v]
            lista.append(k)
    return new_dict
            
    