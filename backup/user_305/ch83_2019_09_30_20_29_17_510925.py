def medias_por_inicial(dic):
    dicm = {}
    dicq = {}
    for k, v in dic.items():
        if k[0] not in dic2.keys():
            dicm[k[0]] = v
            dicq[k[0]] = 1
        else:
            dicm[k[0]] += v
            dicq[k[0]] += 1
    for k,v in dicq.items():
        dicm[k] = dicm[k]/v
    return dicm
            