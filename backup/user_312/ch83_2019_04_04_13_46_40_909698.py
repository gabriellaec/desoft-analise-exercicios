def medias_por_inicial(d):
    dicionario={}
    repetições={}
    for k, v in d.items():
        inicial=k
        if inicial[0] in dicionario:
            dicionario[inicial[0]]+=v
            repetições[inicial[0]]+=1
        else:
            dicionario[inicial[0]]=v
            repetições[inicial[0]]=1
    #print(dicionario)
    for k, v in repetições.items():
        #print(dicionario[k])
        dicionario[k]=dicionario[k]/v
        #print(dicionario[k])
    return dicionario