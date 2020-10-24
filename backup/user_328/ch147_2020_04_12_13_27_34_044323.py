def conta_ocorrencias(lista):
    dict = {}
    for i in lista:
        if i not in dict:
            dict[i]= 1
        elif i in dict:
            dict[i] += 1
    return dict

def mais_frequente(lista):
    x= 0
    dict = conta_ocorrencias(lista)
    for i in dict:
        if dict[i] > x:
            palavra = i
            x = dict[i]
    return palavra
    