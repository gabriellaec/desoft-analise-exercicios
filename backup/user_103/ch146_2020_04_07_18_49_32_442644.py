def conta_ocorrencias(lista):
    dicionario={}
    i=0
    for i in range(len(lista)):
        dicionario[lista[i]]=lista[i].count
    print (dicionario)
        