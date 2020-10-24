def calcula_media(lista):
    c= 0
    soma = 0
    for i in lista:
        for t in i.values():
            soma +=t
            c +=1
            media = soma/c
    return media