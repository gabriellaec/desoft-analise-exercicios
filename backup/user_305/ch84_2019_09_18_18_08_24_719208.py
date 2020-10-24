def inverte_dicionario(dic):
    dic2 = {}
    for k,v in dic.items():
        
        if v in dic2:
            k.append(v)
        dic2[v] = k
    return dic2