def conta_ocorrencias(lista):
    d={}
    for i in lista:
        palavra=lista[i]
        if palavra in d:
            d[palavra]+=1
        else:
            d[palavra]=1
    return d
        