def medias_por_inicial(dic):
    cada_inicial = {}
    for k, v in dic.items():
        cada_inicial[k(0)] = v
    soma = {}
    quantidade = {}
    for k, v in cada_inicial.items():
        if k in soma:
            soma[k] += v
            quantidade[k] += 1
        else:
            soma[k] = v
            quantidade[k] = 1
    media = {}
    for k, v in soma.items():
        q = quantidade[k]
        media[k] = v/q
    return media

            