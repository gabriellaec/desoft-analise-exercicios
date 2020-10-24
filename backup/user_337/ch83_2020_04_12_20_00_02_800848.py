def medias_por_inicial(notas):
    medias = {}
    lista = []
    for i in notas.keys():
        lista.append(i[0])
    for i in notas:
        if not i[0] in medias:
            medias[i[0]] = notas[i]
        else:
            medias[i[0]] += notas[i]
    for a in medias:
        x = lista.count(a)
        medias[a] = medias[a]/x
    return medias