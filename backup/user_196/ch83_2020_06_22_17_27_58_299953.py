def medias_por_inicial(dic):
    dicmedia = {}
    for nome in dic:
        if nome[0] in dicmedia:
            dicmedia[nome[0]] = (dicmedia[nome[0]] + dicmedia[nome])/2
        else:
            dicmedia[nome[0]] = dic[nome]
    return dic