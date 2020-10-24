def conta_ocorrencias(lista):
    dm = {}
    for i in lista:
        if i not in dm:
            dm[i] = 1 
        else: 
            dm[i] +=1
    return dm