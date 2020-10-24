def conta_bigramas(string):
    lista_bigramas = []
    for i in range(len(string) - 1):
        bigramas = (string[i] + string[i + 1])
        lista_bigramas.append(bigramas)
    dic_bigramas = {}
    for bigrama in lista_bigramas:
        if bigrama not in dic_bigramas:
            dic_bigramas[bigrama] = 1
        else:
            if bigrama in dic_bigramas:
                dic_bigramas[bigrama] += 1
    return dic_bigramas