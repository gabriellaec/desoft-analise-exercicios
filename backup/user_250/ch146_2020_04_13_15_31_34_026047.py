def conta_ocorrências(lista):
    dict = {}
    for palavra in lista:
        if palavra not in dict:
            dict[palavra] = 0
        if palavra in dict:
            dict[palavra] += 1
    return dict