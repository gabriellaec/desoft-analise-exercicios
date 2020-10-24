def inverte_dicionario(dic):
    dic2 = {}
    for i in dic:
        if dic[i] not in dic2:
            dic2[dic[i]] = [i] 
        else:
            dic2[dic[i]].append(i) 
    return dic2