def medias_por_inicial (dic):
    dic2={}
    for k,v in dic.items():
        if k[0] not in dic2.Keys():
            dic2[k[0]]=v
        if k[0] in dic2.Keys():
            dic2[k[0]]=(dic2[k[0]]+v)/2
    return dic2 