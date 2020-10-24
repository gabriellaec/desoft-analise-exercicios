def conta_ocorrencias(lista):
    lista=['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
    dicionario=dict()
    for e in lista:
        if not e in dicionario:
            contagem[e]=1
        else:
            contagem[e]+=1
    return dicionario