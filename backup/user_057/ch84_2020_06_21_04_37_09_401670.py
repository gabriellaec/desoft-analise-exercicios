def inverte_dicionario(dic):
    nomes = dic.keys()
    idades = dic.values()
    dic2 = {}
    for i in nomes:
        if idades in dic2:
            dic2[idades] = [dic2[idades], nomes]
        else:    
            dic2[idades] = nomes
    return dic2    