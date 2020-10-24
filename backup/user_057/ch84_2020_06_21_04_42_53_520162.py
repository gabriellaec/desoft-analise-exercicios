def inverte_dicionario(dic):
    idades = dic.values()
    dic2 = {}
    for nome in dic.keys():
        if idades in dic2:
            dic2[idades] = [dic2[idades], nome]
        else:    
            dic2[idades] = nome
    return dic2  