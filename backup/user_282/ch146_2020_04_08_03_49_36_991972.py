def conta_ocorrencias(lista):
    count = dict()
    for palavra in lista:
        if palavra not in count:
            count[palavra] = 1
        else:
            count[palavra] += 1
    return count