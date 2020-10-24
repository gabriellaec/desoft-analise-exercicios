def inverte_dicionario(dic):
    dic2 = {}
    for k,v in dic.items():        
        if v not in dic2:
            dic2[v] = []
        dic2[v].append(k)
    return dic2