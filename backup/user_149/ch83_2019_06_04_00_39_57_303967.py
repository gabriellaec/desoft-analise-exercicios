def medias_por_inicial(dicionario):
    saida = {}
    for k,v in dicionario.items():
        dicionario[k]=k[0]
        saida[k[0]]=v
    return saida