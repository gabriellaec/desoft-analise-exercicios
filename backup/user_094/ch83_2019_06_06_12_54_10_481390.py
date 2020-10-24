def medias_por_inicial(dic):
    dic1 = {}
    dic2 = {}
    for k,v in dic:
        if k[0] in dic1:
            dic1[k[0]] += v
            dic2[k[0]] += 1
        else:
            dic1[k[0]] = v
            dic2[k[0]] = 1
    for k in dic1:
        dic1[k] = dic1[k]/dic2[k]
    return dic1