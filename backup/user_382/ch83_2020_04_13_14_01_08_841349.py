def medias_por_inicial(dic):
    dic2 = {}
    for i in dic:
        if i[0] not in dic2:
            c = 1 
            dic2[i[0]] = [dic[i],c]    
        else:
            c += 1
            dic2[i[0]] += [dic[i],c]
            
    
    for k in dic2:
        dic2[k] = dic2[k][0]/dic2[k][1]
    return dic2 