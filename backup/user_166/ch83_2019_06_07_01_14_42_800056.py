def medias_por_inicial(dic):
    dic_notas_inicial={}
    for nomes in dic:
        if nomes[0] not in dic_notas_inicial:
        	dic[nomes[0]]= 1
        else:
            dic[nomes[0]] +=1
    return dic_notas_inicial        
        