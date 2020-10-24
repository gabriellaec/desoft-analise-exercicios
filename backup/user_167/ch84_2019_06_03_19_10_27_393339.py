def inverte_dicionario  (dic):
    n_dic={}
    for k,v in dic.items():
        n_dic[v]='{0}'.format(k)
    return n_dic
        
        