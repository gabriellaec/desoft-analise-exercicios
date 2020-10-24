def medias_por_inicial(x):
    dic = {}
    for e,k in x.items():
        if e[0] in dic:
            dic[e[0]] += k
            dic[e[0]] = dic[e[0]]/2 
        else:    
            dic[e[0]] = k
    return dic