def calcula_media(lista):
    cont= 0
    soma= 0
    for i in lista:
        for v in i.values():
            soma = soma + v
            cont = cont + 1
            media= soma/cont
    return media