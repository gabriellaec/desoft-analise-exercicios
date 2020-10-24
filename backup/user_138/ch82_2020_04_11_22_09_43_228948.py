def primeiras_ocorrencias(string):
    dcionario={}
    i=0
    for a in string:
        if a not in dicionario:
            dicionario[a]=i
        else:
            i+=1
    return dicionario