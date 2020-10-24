def primeiras_ocorrencias(string):
    dicionario={}
    i=0
    for a in string:
        if a not in dicionario:
            dicionario[a]=i
        else:
            i+=1
    return dicionario