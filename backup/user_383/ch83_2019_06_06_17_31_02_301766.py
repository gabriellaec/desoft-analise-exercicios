def medias_por_inicial(dicionario):
    dic={}
    for k,v in dicionario.items():
        dic[k[0]] = v
        for m,n in dicionario.items():
            if k[0] == m[0]:
                dic[k[0]] += (n-v)/2
    return dic