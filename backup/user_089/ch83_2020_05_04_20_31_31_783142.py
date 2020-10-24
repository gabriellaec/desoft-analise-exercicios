def medias_por_inicial(dic):
    dic2 = {}
    for k,v in dic.items():
        if k[0] not in dic2:
            dic2[k[0]] = [v]
        else:
            dic2[k[0]] += [v]
    for i,x in dic2.items():
        dic2[i] = sum(x)/len(dic2[i])
    return dic2