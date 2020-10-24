def inverte_dicionario(dicionario):
    new_dict = {}
    for k, v in dicionario.items():
        if v not in new_dict.keys():
            lista = [dicionario[k]]
            new_dict[v] = lista
        else:
            lista.append(dicionario[k])
    return new_dict
            
    