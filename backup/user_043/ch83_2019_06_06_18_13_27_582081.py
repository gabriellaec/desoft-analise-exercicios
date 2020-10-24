def medias_por_inicial(dicionario):
    dict2 = {}
    dict3 = {}
    for k, v in dicionario.items():
        if k[0] in dict2:
            dict2[k[0]].append(v)
            dict3[k[0]] += 1
        else:
            dict2[k[0]]=[]
            dict2[k[0]].append(v)
            dict3[k[0]] = 1
    for k, v in dict2.items():
        soma=0
        for i in v:
            soma+=i
        dict3[k]=soma/len(v)
    return dict3