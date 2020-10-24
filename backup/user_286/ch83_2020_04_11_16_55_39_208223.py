def medias_por_inicial(dic):
    dic_medias = {}
    for nome, nota in dic.items():
        if nome[0] not in dic_medias.keys():
            dic_medias[nome[0]] = nota
        else:
            for nome_, nota_ in dic_medias.items():
                if nome[0] == nome_[0]:
                    dic_medias[nome[0]] = (dic_medias[nome[0]] + nota) /2

    return dic_medias