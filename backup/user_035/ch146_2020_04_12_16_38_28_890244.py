def conta_ocorrencias(lista):
    dic = {}
    for i in range(len(lista)):
        if lista[i] not in dic:
            dic(lista[i]) = 1
        else:
            dic(lista[i]) += 1
    return dic 