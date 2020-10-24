def primeiras_ocorrencias(palavra):
    list(palavra)
    dicionario={}
    i=0
    for i in range (len(palavra)):
        if not palavra[i] in dicionario:
            dicionario[palavra[i]]=i
    return dicionario
                                 