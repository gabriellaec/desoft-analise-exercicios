def medias_por_inicial(entrada):
    dic = {}
    for k, v in entrada.items():
       
        a = k
        b = v
        
        if a[0] not in dic:
            dic[a[0]] = b
        else: 
            dic[a[0]] = (dic[a[0]] +b)/2
    return dic
