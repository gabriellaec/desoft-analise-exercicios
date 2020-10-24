def inverte_dicionario(dic):
    dic2 = {}
    for idade in dic.values():
        nome = dic.keys()
        if idade in dic2:
            dic2[idade].append(dic[nome])
        else:
            dic2[idade] = dic[nome]
    return dic2            