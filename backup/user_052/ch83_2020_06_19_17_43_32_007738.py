def medias_por_inicial(dicionario):
    novo={}
    contador={}
    for i in dicionario:
        if i[0] not in novo:
            novo[i[0]]=dicionario[i]
            contador[i[0]]=1
        else:
            novo[i[0]]+=dicionario[i]
            contador[i[0]]+=1
    for e,v in novo.items():
        novo[e]=v/contador[e]
    return novo