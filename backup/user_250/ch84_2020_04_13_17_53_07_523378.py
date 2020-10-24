def inverte_dicionario(dict1):
    dict2 = {}
    for k,v in dict1:
        dict2[dict2[v]] = dict2[k]
    return dict2