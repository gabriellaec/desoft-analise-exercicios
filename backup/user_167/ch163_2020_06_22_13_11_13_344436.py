def calcula_media (lista):
    for e in lista:
        for v in e.values():
            sum+=v
        media=(sum/(len(lista)+1))
    return media