def conta_ocorrencias(lista):
    dicionario={}
    i=1
    for palavra in lista:
        dicionario[palavra]=i
        i+=1
    return dicionario
