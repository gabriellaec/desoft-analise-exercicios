def conta_ocorrencias(lista):
    dicio = {}
    for i in lista:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
        
    return dicio