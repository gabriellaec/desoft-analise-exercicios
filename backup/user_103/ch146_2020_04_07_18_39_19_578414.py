def conta_ocorrencias(lista):
    dicionario={}
    i=1
    for i in range(len(lista)):
        dicionario[lista[i]]=i
    return dicionario
        