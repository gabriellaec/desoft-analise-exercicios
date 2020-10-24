def medias_por_inicial(dicionario):
    dicionario2={}
    contador={}
    for i in dicionario:
        if i[0] not in dicionario2:
            dicionario2[i[0]]=dicionario[i]
            contador[i[0]]=1
        else:
            dicionario2[i[0]]+=dicionario[i]
            contador[i[0]]+=1
    for e,v in dicionario2.items():
        dicionario2[e]=v/contador[e]
    return dicionario2
        
        
    