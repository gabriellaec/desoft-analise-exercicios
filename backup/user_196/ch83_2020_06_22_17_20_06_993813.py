def medias_por_inicial(dic):
    soma = 0
    qnt = 0
    dicmedia = {}
    for i in dic.keys():
        for inicial in i:
            if inicial == inicial:
                soma+= dic.values(inicial)
                qnt +=1
                media = soma/qnt
            dicmedia[inicial] = media
    return dicmedia