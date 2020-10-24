def conta_ocorrencias(lista):
    dicionario={}
    for i in range(len(lista)):
        dicionario[lista[i]]=i+1
    return dicionario
        