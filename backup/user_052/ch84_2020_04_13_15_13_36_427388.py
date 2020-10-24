def inverte_dicionario(dic):
    a = dic.values()
    b = dic.keys()
    dicionario = {}
    for a in dic:
        for b in dic:
            dic(a) = b
    return dic
        
        