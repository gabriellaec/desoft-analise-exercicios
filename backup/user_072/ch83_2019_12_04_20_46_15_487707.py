def medias_por_inicial(dicionario):
    dicionario2={}
    i=1
    soma=0
    for c in dicionario:
        if c[0] not in dicionario2:
            dicionario2[c[0]]=dicionario[c]
            soma=dicionario[c]
        else:
            i+=1
            soma+=dicionario[c]
            dicionario2[c[0]]=soma/i
    return dicionario2