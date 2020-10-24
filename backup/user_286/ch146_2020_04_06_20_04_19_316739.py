def conta_ocorrencias(lista):
    dict = {}
    for item in lista:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1
        
    return dict