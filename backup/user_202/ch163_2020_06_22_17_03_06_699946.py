def calcula_media(alunos):
    media = 0
    quantidade_de_notas = 0
    for sala in alunos:
        for nota in sala.values():
            media += nota
            quantidade_de_notas += 1
    media /= quantidade_de_notas
    return media
    