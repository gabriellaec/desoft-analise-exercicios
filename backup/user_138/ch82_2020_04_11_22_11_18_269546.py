def primeiras_ocorrencias(string):
    dicionario={}
    i=0
    for a in string:
        if a not in string:
            dicionario[a]=i
            i+=1
        else:
            i+=1
    return dicionario