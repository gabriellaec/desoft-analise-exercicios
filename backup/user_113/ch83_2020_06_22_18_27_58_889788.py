def medias_por_inicial(nomes):
    media = {}
    i=1
    for i in nomes:
        if nomes[i][0] == nomes[i-1][0]:
            media.append([i],[0])
        elif nomes[i][0] != nomes[i-1][0]:
            media.append([i],[0])
    return media