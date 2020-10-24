def medias_por_inicial (dic1): #dicionario de nomes
    dic2 = {} #dicionario de medias
    media = 0
    for k,v in dic1.items():
        if k[0] in dic2:
             dic2[k[0]].append(v)
        else:
             dic2[k[0]] = [v] 