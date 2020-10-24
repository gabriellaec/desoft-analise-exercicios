def calcula_media(lis):
    notas = []
    for dic in lis:
        for nota in dic.values():
            notas.append(nota)
    media = 0
    for nota in notas:
        media += nota
    return media/len(notas)
