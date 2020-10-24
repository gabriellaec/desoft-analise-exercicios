def conta_ocorrencias(lista):
    d = {}
    for i in range(len(lista)):
        if lista[i] not in d:
            d[lista[i]] = 1
        else:
            d[lista[i]] +=1
    return d

def mais_frequente(lista):
    x = conta_ocorrencias(lista)
    y = list(x.items())
    print(y)
    j = y[0][0]
    for i in range(len(y)-1):
        if y[i+1][1]>y[i][1]:
            j = y[i+1][0]
    return j