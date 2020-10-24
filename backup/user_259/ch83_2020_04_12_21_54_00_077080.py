def medias_por_inicial(dic):
    lista =[]
    medias = {}
    media = 0
    for i in dic.keys():        
        medias[i[0]] = media    
    for i in dic.keys():   
        lista.append(i[0])    
    ocorrencias = {}
    for i in lista:
        ocorrencias[i] = 0
    for i in lista:
        if i in ocorrencias:
            ocorrencias[i]+=1
    for i in dic:
        vezes = ocorrencias[i[0]]
        if i[0] in medias:
            medias[i[0]]+=dic[i]/vezes
            
    return medias
