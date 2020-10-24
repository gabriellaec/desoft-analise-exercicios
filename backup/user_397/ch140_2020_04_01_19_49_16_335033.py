def faixa_notas (lista):
    notas_baixas = 0
    notas_medias = 0
    notas_altas = 0
    for nota in lista:
        if nota<5:
            notas_baixas += 1
        elif nota<=7:
            notas_medias += 1
        else:
            notas_altas += 1
    lista_total = [notas_baixas, notas_medias, notas_altas]
    return lista_total
    