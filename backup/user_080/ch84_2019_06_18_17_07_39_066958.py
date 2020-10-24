def inverte_dicionario(dic_string):
    dic={}
    for i in dic_string.keys():
        if dic_string[i] not in dic.keys():
            dic[dic_string[i]]=[]
        dic[dic_string[i]].append(i)
        
    return dic
            
        