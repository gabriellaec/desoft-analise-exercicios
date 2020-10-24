def medias_por_inicial(dic):
    saida = {}
    i = 0 
    for k in dic.keys():
        saida.append([k][0])
    for v in dic.values():
        saida.append(v)
    return saida
    