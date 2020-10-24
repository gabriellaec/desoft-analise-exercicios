def inverte_dicionario(dic):
    dic2 = {}   
    for k,v in dic.items():
        if v in dic2:
            dic2[v] += [k]
        else:
            dic2[v] = [k]
    return dic2
