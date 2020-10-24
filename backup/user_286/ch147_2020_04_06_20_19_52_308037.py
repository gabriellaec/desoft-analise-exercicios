def conta_ocorrencias(lista):
    dict = {}
    for item in lista:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1
        
    return dict

def mais_frequente(lista):
    dict = conta_ocorrencias(lista)
    i = 0
    lista = list(dict.values())
    for item in dict.keys():
        if dict[item] == max(lista):
            return str(item)