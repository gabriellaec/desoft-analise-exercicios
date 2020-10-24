def medias_por_inicial(dic):
    notas = {}
    media = {}
    for i, n in dic.items():
        if i[0] not in media:
            media[i[0]] = n
            notas[i[0]] = 1
        else:
            media[i[0]] = notas[i[0]] * media[i[0]] + n
            notas[i[0]] += 1
            media[i[0]] = media[i[0]] / notas[i[0]]
    return media