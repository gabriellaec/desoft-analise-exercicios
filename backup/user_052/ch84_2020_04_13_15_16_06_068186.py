def inverte_dicionario(dic):
    a = dic.values()
    b = dic.keys()
    dicionario = {}
    for a in dic:
        for b in dic:
            dicionario[a] = b
    return dicionario
        
        