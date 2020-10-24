def conta_ocorrencias(lista):
    dict = {}
    for i in lista:
        if i not in dict:
            dict[i]= 1
        elif i in dict:
            dict[i] += 1
    return dict