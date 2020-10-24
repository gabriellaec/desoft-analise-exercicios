def calcula_media(lista):
    soma=0
    n=0
    for i in lista:
        dicio=i
        for e in dicio.values():
            soma=soma+e
            n=n+1
    media=soma/n
    return media
        