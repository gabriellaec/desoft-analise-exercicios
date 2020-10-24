def acha_bigramas(string):
    lista_bigramas = []
    i=0
    bigrama = string[i] + string[i+1]
    for bigrama in string:
        if bigrama not in lista_bigramas:
            lista_bigramas.append(bigrama)
        if bigrama in lista_bigramas:
            continue
    return lista_bigramas
        