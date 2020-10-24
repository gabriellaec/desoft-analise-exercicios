def medias_por_inicial(dic):
    novodic = {}
    dicfinal = {}
    for x, v in dic.items():
        inicial = x[0]
        if not inicial in novodic.values():
            novodic[inicial]=[v]
        else:
            novodic[inicial].append(v)
    for e in novodic:
        valores = novodic[e]
        i=0
        soma = 0
        while i<len(valores):
            soma+=valores[i]
            i+=1
        media = soma/i
        dicfinal[e]=media
    return dicfinal