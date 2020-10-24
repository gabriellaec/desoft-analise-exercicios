def inverte_dicionario(x):
    dic = {}
    for e,k in x.items():

        if k in dic:
            dic[k].append(e)
        else:
            dic[k] = [e]
    return dic
            
     
   