def faixa_notas(lista):
    num_baixas = 0
    num_medias = 0
    num_altas = 0
    for nota in lista:
        if nota < 5:
            num_baixas +=1
        elif 5 <= nota <= 7:
            num_medias +=1
        else:
            num_altas +=1
    lista_final = [num_baixas, num_medias, num_altas]
    return lista_final