def medias_por_inicial(dic):
    medias = {}
    numeros = {}
    for i,nota in dic.items():
        if i[0] not in medias:
            medias[i[0]] = nota
            numeros[i[0]] = 1
        else:
            medias[i[0]] = numeros[i[0]]*medias[i[0]] + nota
            numeros[i[0]] += 1
            medias[i[0]] = medias[i[0]]/numeros[i[0]]
        return medias