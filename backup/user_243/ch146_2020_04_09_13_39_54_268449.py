def conta_ocorrencias(lista):
    d={}
    for i in lista:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        return d