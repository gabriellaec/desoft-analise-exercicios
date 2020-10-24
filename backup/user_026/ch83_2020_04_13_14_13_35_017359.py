def medias_por_inicial(dic):
    soma = {}
    quant = {}
    for k, v in dic.items():
        if k[0] in soma:
            soma [k[0]] +=v
            quant[k[0]]+=1
        else:
            soma[k[0]] = v
            quant[k[0]]+=1
    media = {}
    for k, v in soma.items():
        q = quant[k]
        media[k] = v/q
    return media