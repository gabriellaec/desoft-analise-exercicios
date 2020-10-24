def inverte_dicionario(dict):
    dic={}
    for k,v in dict.items():
        if v not in dic:
        	dic[v]=[k]
        dic[v].append(k)
    return dic
      
            