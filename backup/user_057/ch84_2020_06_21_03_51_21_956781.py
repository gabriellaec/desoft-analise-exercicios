def inverte_dicionario(dic):
    dic2 = {}
    for idade in dic.values():
        if idade in dic2:
            dic2[idade].append(dic[nome])
        else:
            dic2[idade] = dic[nome]
        
    return dic2            