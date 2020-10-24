def acha_bigramas(palavra):
    lista_bigramas = []
    t = 0

    while t < (len(palavra) - 1):
            bigrama = palavra[t] + palavra[t + 1]
            lista_bigramas.append(bigrama)
            t += 1

    lista_bigramas = list(dict.fromkeys(lista_bigramas))

    return lista_bigramas
