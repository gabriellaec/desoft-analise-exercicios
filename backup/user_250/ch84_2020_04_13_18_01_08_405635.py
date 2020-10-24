def inverte_dicionario(dict1):
    dict2 = {}
    for k in dict1:
        if dict1[k] not in dict2:
            dict2[dict1[k]] = [k]
        else:
            dict2[dict1[k]].append(i)
    return dict2