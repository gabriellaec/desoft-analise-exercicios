def medias_por_inicial(entrada):
    dic = {}
    for k, v in entrada.items():
       
        a = k
        
        if a[0] not in dic:
            dic[a[0]] = v
        else: 
            dic[a[0]] = (dic[a[0]] + v)/2
    return dic