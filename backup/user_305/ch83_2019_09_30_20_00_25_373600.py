def medias_por_inicial(dic):
    dic2 = {}
    s = 1
    for k, v in dic.items():
        if k[0] not in dic2.keys():
            dic2[k[0]] = v
        else:
            dic2[k[0]] += v
            s += 1
    dic2[k[0]] = v/s
    return dic2
            