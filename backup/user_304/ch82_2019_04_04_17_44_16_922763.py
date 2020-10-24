def primeiras_ocorrencias(palavra):
    dicionario={}
    i=0
    while i<len(palavra):
        if palavra[i] not in dicionario:
            dicionario[palavra[i]]=i
    return dicionario