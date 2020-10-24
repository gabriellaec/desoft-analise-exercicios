def calcula_media (lista):
    sum=0
    for e in lista:
        for v in e.values():
            sum+=v
        media=(sum/(len(lista)+1))
    return media