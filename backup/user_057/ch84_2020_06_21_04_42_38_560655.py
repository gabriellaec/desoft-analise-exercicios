def inverte_dicionario(dic):
    idades = dic.values()
    dic2 = {}
    for nome in dic.keys():
        if idades in dic2:
            dic2[idades] = [dic2[idades], nomes]
        else:    
            dic2[idades] = nomes
    return dic2  