def medias_por_inicial(dic):
    dic2 = {}
    dicvalor = {}
    for k,v in dic.items():
        if k[0] in dic2.keys():
        	dic2[k[0]] += v
            dicvalor[k[0]] +=1
        else:
            dic2[k[0]] = v
    		dicvalor[k[0]] = 1
    dic2[k[0]] = dic2[k[0]]/dicvalor[k[0]]
    return dic2
        
        
