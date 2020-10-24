def conta_ocorrencias(lista):
    dicio = {}
    for i in range(len(lista)):
        dicio[i] = lista.count(i)
    
    return dicio