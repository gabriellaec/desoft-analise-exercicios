def conta_ocorrencias(lista):
    dicionario={}
    i=0
    for i in range(len(lista)):
        dicionario[lista[i]]=str(lista[i]).count
    return dicionario
        