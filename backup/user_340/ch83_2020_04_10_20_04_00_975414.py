def medias_por_inicial(dicionario):
    dicionario1={}
    for t,i in dicionario.items():
        if t[0] in dicionario1:
            dicionario1[t[0]]+=i
        else:
            dicionario1[t[0]]=i
    return dicionario1
            
        