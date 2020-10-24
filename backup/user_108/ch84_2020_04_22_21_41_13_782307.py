def inverte_dicionario(dic):
    new_dic = {} 
    for key in dic:
        new_dic[dic[key]] = dic.get(key,[])
        new_dic[dic[key]].append(key)
    return new_dic