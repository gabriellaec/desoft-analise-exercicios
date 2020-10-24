def acha_bigramas(string):
    lista_bigramas = []
    i=0
    for i in string:
        bigrama = string[i] + string[i+1]
        if bigrama not in lista_bigramas:
            lista_bigramas.append(bigrama)
        if bigrama in lista_bigramas:
            continue
    return lista_bigramas
        