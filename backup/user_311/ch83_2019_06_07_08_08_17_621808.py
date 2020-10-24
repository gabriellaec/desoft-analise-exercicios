def medias_por_inicial(medias):
    dic_medias = {}
    for k, v in medias.items():
        dic_medias[k[0]] = v
        for m, n in medias.items():
            if k[0] == m[0]:
                dic_medias[k[0]] += n-v/2
    return dic_medias