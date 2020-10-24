def primeiras_ocorrencias (string):
    lista = []
    dic = {}
    for i in range(len(string)):
        lista.append(string[i])
    for item in lista:
        dic [item] = lista.index(item)
    return dic
        