def conta_ocorrencias(lista):
    dn={}
    for i in range(len(lista)):
        dn[lista[i-1]]=i
    return dn
        