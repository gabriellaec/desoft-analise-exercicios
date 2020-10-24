def medias_por_inicial(notas):
    medias = {}
    lista = []
    for i in notas.keys():
        lista.append(i[0])
    for i in notas:
        if not i[0] in medias:
            medias[i[0]] = notas[i]
        else:
            x = lista.count(i[0])
            medias[i[0]] = (medias[i[0]] + notas[i])/x
    return medias
        