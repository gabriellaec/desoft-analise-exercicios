def calcula_media(x):
    z = []
    for i in range(len(x)):
        for nota in x[i].values():
            z.append(nota)
    media = (sum(z))/(len(z))
    return media
            