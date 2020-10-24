def inverte_dicionario(dicionario):
    dic={}
    for k,v in dicionario.items():
        dic[v]=dic.get(v,[])
        dic[v].append(k)
    return dic
    
    
    
    
  