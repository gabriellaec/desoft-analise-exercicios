def medias_por_inicial(dicionario):
    dicionario2={}
    contador={}
    for i in dicionario:
        if i[0] not in dicionario2:
            dicionario2[i[0]]=dicionario[i]
            contador[i[0]]=1        
        else:
            dicionario2[i[0]]+=(dicionario[i])
            contador[i[0]]+=1

    for i,e in dicionario2.items():
            dicionario2[i]= e/contador[i]



        

    return dicionario2

    