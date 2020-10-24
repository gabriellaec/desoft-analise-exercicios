def medias_por_inicial(dic):
    dic2={}
    for k,v in dic.items():
        dic2[k[0]] = dic2.get(k[0],0) + v
    
    return dic2
print(medias_por_inicial(dic))   
