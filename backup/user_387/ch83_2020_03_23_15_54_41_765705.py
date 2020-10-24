def medias_por_inicial(a):
    dic={}
    for key in a:
        if key[0] not in dic:
            dic[key[0]] = a[key]
        else: 
            dic[key[0]] = (dic[key[0]] + a[key])/2 

    return dic