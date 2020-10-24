def conta_ocorrencias(lista):
    dn={}
    for i in range(len(lista)):
        dn[lista[i-1]]=(i+1-2)
    return dn
        