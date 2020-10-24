def conta_ocorrencias(lista):
    dicio = {}
    for i in lista:
        if lista[i] in dicio:
            dicio[lista[i]] += 1
        else:
            dicio[lista[i]] = 1
        
    return dicio