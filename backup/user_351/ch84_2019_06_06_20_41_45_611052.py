def inverte_dicionario (dic):
    dict={}
    for k,v in dic.items():
        if v not in dic:
        	dic[v]=[k]
        dict[v].append(k)
    return dict
      
            