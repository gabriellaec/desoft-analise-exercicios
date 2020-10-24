def medias_por_inicial(dic):
    dic2 = {}
    dic_count = {}
    for i in dic:
        if i[0] not in dic2:
            dic2[i[0]] = dic[i]
            dic_count[i[0]] = 1
        else:
            dic2[i[0]] += dic[i]
            dic_count[i[0]] += 1
    
    for k,v in dic2.items():
        dic2[k] = v/dic_count[k]
    return dic2 