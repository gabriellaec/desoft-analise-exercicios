def medias_por_inicial(nome_para_nota):
    letra_para_media = {}
    for nome, nota in nome_para_nota.items():
        if not nome[0] in letra_para_media:
            letra_para_media[nome[0]] = nota
        else:
            letra_para_media[nome[0]] = letra_para_media[nome[0]]/len(nota)
    return letra_para_media