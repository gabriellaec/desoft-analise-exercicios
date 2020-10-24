def medias_por_inicial(notas):
    medias = {}
    for i in notas:
        if not i[0] in medias:
            medias[i[0]] = notas[i]
        if i[0] in medias:
            x = notas[i] + 