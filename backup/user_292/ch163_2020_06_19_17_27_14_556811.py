def calcula_media(lista):
    notas = 0
    q = 0
    for i in lista:
        for x in i.values():
            notas += x
            q += 1 
    media = notas/q       
    return media
    
