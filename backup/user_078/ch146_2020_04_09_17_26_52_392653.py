def conta_ocorrencias(lista):
    dic={}
    for palavra in lista:
        dic[palavra] = lista.count(palavra)
    return dic