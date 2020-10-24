def inverte_dicionario(dicionario):
    new_dict = {}
    for k, v in dicionario.items():
        if v not in new_dict.keys():
            new_dict[v] = dicionario[k]
        else:
            new_dict[v] += dicionario[k]
    return new_dict
            
    