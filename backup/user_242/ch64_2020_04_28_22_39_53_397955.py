def acha_bigramas(string):
    lista_bigramas = []
    i=0
    bigrama = string[i] + string[i+1]
    for bigrama in string:
        if bigrama in lista_bigramas:
            continue
        if bigrama not in lista_bigramas:
            lista_bigramas.append(bigrama)
    return lista_bigramas
        