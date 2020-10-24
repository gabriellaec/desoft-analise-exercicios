def medias_por_inicial(dic):
    medias = {}
    numeros = {}
    for i,nota in dic.items():
        if i not in medias:
            medias[i] = nota
            numeros[i] = 1
        else:
            medias[i] = numeros[i]*medias[i] + nota
            numeros[i] += 1
            medias[i] = medias[i]/numeros[i]
    return medias