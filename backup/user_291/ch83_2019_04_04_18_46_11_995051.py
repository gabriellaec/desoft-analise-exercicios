def medias_por_inicial(notas):
    media_notas = {}
    i = 1
    for e in notas:
        if e[0] in media_notas:
            media_notas[e[0]] = (media_notas[e[0]]+notas[e])/(i+1)
            i += 1
        else:
            media_notas[e[0]] = notas[e]
            
    return media_notas