def conta_ocorrencias(lista):
    a = len(lista)
    dic= {}
    for i in range(a):
        a = lista[i]
        dic[a] = i + 1
    return dic
        
        