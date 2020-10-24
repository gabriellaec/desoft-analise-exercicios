def faixa_notas(lista):
    inferiores= 0
    media= 0
    maiores= 0
    for i in lista:
        if i < 5:
            inferiores += 1
        elif i <= 7:
            media += 1
        else:
            maiores += 1
    notas_finais= [inferiores, media, maiores]
    return notas_finais 