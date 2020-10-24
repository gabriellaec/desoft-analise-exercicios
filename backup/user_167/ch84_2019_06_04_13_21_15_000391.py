def inverte_dicionario  (dic):
    n_dic={}
    for k,v in dic.items():
        if v in n_dict:
            n_dict[v].append(k)
        else:
            n_dict[v]=[k]
    return n_dict
        
        