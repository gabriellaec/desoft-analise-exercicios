def conta_ocorrencias(lista):
    dict = {}
    for palavra in lista:
        if palavra not in dict:
            dict[palavra] = 0
        if palavra in dict:
            dict[palavra] += 1
    return dict

def mais_frequente(lista):
    dict2 = conta_ocorrencias(lista)
    max = 0
    for k in dict2:
        if dict2[k] > max:
            max = k
    return max