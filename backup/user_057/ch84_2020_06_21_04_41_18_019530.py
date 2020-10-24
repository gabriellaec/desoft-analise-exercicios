def inverte_dicionario(dic):
    nomes = dic.keys()
    idades = dic.values()
    dic2 = {}
    i=0
    while i in range(len(nomes)):
        if idades in dic2:
            dic2[idades] = [dic2[idades], nomes[i]]
        else:    
            dic2[idades] = nomes[i]
        i =+ i
    return dic2    