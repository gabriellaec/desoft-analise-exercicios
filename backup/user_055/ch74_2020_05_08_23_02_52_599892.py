def conta_bigramas(string):
    lista_bigramas = []
    for i in range(len(string) - 1):
        bigramas = (string[i] + string[i + 1])
        if bigramas not in lista_bigramas:
            lista_bigramas.append(bigramas)
    dic_bigramas = {}
    for bigramas in lista_bigramas:
        if bigramas not in dic_bigramas:
            dic_bigramas[bigramas] = 1
        else:
            dic_bigramas[bigramas] += 1
    return dic_bigramas