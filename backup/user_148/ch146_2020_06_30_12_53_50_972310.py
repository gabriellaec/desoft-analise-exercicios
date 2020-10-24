def conta_ocorrencias(lista):
    dic = {}
    for i in lista:
        dic[i] = lista.count(i)
    
    return dic
