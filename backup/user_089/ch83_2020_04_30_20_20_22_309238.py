def medias_por_inicial(dic):
    dic2 = {}
    for k,v in dic.items():
        if k[0] not in dic2:
            dic2[k[0]] += [v]/len(dic2[k[0]])
        else:
            dic2[k[0]] = [v]/len(dic2[k[0]])
    return dic2