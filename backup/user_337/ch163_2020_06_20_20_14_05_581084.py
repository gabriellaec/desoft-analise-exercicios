def calcula_media(lista):
    soma = 0 
    i = 0
    for sala in lista:
        for nota in sala.values():
            soma += nota
            i += 1
    media = soma/i
    return media