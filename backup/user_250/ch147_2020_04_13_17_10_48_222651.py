def conta_ocorrencias(lista):
    dict = {}
    for palavra in lista:
        if palavra not in dict:
            dict[palavra] = 0
        if palavra in dict:
            dict[palavra] += 1
    return dict

def mais_frequente(lista):
    dict = conta_ocorrencias(lista)
    Max = max(dict, key=dict.get)
    return Max