def conta_ocorrencias(lista):
    dicionario={}
    for i in lista:
        if lista[i] in dicionario:
            dicionario[i]+=1
        else:
            dicionario[i]=1
    return dicionario