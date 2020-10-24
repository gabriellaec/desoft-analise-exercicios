def conta_ocorrencias(lista):
    dic= {}
    for palavra in lista:
        if palavra not in lista:
            dic[palavra] = 1
        else:
            dic[palavra] +=1
    return dic
