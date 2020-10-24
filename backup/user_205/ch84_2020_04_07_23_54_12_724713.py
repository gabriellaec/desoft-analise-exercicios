def inverte_dicionario (dic): 
    inverte = {}
    for chave in dic.keys():
        for valores in dic.values():
            inverte[valores]=dic[valores]
    return inverte