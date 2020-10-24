def medias_por_inicial(x):
    dic = {}
    for e in x:
        for k in e:
            dic[e[0]] = k
    return dic