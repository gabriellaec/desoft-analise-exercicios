def acha_bigramas(string):
    lista_bigramas = []
    for i in range(len(string) - 1):
        bigramas = (string[i] + string [i + 1])
        if bigramas not in lista_bigramas:
            lista_bigramas.append(bigramas)
    return lista_bigramas
        