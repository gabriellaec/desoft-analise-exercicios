def conta_ocorrencias(lista):
    d = {}
    for i in range(len(lista)):
        if lista[i] not in d:
            d[lista[i]] = 1
        else:
            d[lista[i]] +=1
    return d