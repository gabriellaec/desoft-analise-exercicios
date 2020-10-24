def faixa_notas(li):
    num_baixas = 0
    num_medias = 0
    num_altas = 0
    for nota in li:
        if nota < 5:
            num_baixas += 1
        elif nota <= 7:
            num_medias += 1
        else:
            num_altas += 1
    lista_final = [num_baixas, num_medias, num_altas]
    return lista_final

            