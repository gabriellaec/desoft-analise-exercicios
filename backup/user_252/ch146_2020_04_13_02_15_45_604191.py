def conta_ocorrencias(lista):
    d={}
    i=0
    for i in range(len(lista)):
        palavra=lista[i]
        if palavra in d:
            d[palavra]+=1
        else:
            d[palavra]=1
    return d
        