def conta_ocorrencias(lista):
    ocorrencias = {}
    for i in lista:
        ocorrencias[i] = 0
    for i in lista:
        if i in ocorrencias:
            ocorrencias[i]+=1
    return ocorrencias
        