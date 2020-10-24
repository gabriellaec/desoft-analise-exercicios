def primeiras_ocorrencias (string):
    lista = []
    dic = {}
    for i in range(len(string)):
        lista.append(string[i])
    for item in lista:
        dicionario [item] = lista.count(item)
    return dicionario
        