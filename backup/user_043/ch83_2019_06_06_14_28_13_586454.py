def medias_por_inicial(dicionario):
    dict2 = {}
    for k, v in dicionario.items():
        if k[0] in dict2:
            dict2[k[0]].append(v)
        else:
            dict2[k[0]]=[]
            dict2[k[0]].append(v) 
    for k, v in dict2.items():
        soma=0
        for i in v:
            soma+=i
        v=soma/len(v)
    return dict2