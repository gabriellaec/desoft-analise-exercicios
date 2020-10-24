def conta_ocorrencias(lista):
    d = {}
    for i in range(len(lista)):
        if lista[i] not in d:
            d[lista[i]] = 1
        else:
            d[lista[i]] +=1
    return d

def mais_frequente(lista):
    j = 0
    x = conta_ocorrencias(lista)
    y = max(list(x.values()))
    for i in range(len(x)):
        if x[i] == y:
            j = x[i]
    return j