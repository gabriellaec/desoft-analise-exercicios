def calcula_media(lista):
    contador = 0 
    soma = 0
    for i in lista:
        for v in i.values():
            soma+=v
            contador+=1
            media = soma/contador
    return media