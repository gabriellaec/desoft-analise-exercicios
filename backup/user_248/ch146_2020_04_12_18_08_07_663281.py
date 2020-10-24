def conta_ocorrencias(lista):
    lista=['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
    dicionario=dict()
    for e in lista:
        if not e in dicionario:
            lista[e]=1
        else:
            lista[e]+=1
    return dicionario