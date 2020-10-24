def conta_ocorrencias(lista):
    dic={}
    for i in lista:
        if lista[i] in dic:
            dic[lista[i]] += 1
        else:
            dic[lista[i] = 1