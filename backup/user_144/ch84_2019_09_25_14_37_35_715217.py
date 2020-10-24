def inverte_dicionario(dic):
    dic = {}
    for k,i in dict.items():
        if i not in dic:
            dic[i] = [k]
        else:
            dic[i].append(k)
            
    return dic