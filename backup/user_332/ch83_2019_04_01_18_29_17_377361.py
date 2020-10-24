def medias_por_inicial (dic):
    dic1 = {}
    
    for a, b in dic.items():
        soma = 0
        i = 2
        if a[0] in dic1:
            dic1[a[0]] += b
            dic1[a[0]] /= i
            i += 1
            
        else:
            dic1[a[0]] = b
    
    return dic1