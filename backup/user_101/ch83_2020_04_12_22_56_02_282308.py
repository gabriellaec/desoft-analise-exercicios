def medias_por_inicial(dic):
    saida = {}
    for k, v in dic.items():
        if k[0] in saida:
            saida[k[0]] += 1
        else:
            saida[k[0]] = 1
    return saida