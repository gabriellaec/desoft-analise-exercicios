def medias_por_inicial(x):
    saida = {}
    i = 0 
    for k in x.keys():
        saida.append([k][0])
    for v in x.values():
        saida.append(v)
    return saida
    