def primeiras_ocorrencias(palavra):
    dicionario={}
    for i in range(0,len(palavra)):
        if palavra[i] not in dicionario:
            dicionario[palavra[i]]=i
    return dicionario