def acha_bigramas(estringui):
    i = 0
    bigrama = ""
    lista_bigramas = []
    while (i < len(estringui)-1):
        bigrama = estringui[i]+estringui[i+1]
        if(bigrama in lista_bigramas):
            i = i + 1
        else:
            lista_bigramas.append(bigrama)
        i = i + 1
    return lista_bigramas