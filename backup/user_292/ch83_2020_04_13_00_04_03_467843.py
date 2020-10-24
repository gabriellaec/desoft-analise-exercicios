def medias_por_inicial(di):
    media = {}
    x = {}
    for nome, nota in di.items():
        if nome[0] not in media:
            media[nome[0]] = nota
            x[nome[0]] = 1
        else:
            media[nome[0]] = media[nome[0]] + nota
            x[nome[0]] += 1
            media[nome[0]] = media[nome[0]]/x[nome[0]]
    return media