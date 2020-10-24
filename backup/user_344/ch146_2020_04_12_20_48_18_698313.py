def conta_ocorrencias(lista):
    dic= {}
    for palavra in lista:
        if palavra in lista:
            dic[palavra] +=1
    return dic
