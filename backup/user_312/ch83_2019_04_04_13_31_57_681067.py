def medias_por_inicial(d):
    dicionario={}
    repetições={}
    for k, v in d.items():
        inicial=k
        if inicial[0] in d:
            dicionario[inicial[0]]+=v
            repetições[inicial[0]]+=1
        else:
            dicionario[inicial[0]]=v
            repetições[inicial[0]]=1
    for k, v in repetições.items():
        dicionario[k]=dicionario[k]/v
    return dicionario