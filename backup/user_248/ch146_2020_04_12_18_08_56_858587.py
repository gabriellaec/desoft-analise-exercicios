def conta_ocorrencias(lista):
    dicionario=dict()
    for e in lista:
        if not e in dicionario:
            dicionario[e]=1
        else:
            dicionario[e]+=1
    return dicionario