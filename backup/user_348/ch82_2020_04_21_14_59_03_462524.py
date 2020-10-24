def primeiras_ocorrencias(string):
    dicionario = {}
    i = 0
    while i<len(string):
        if string[i] not in dicionario.keys():
            dicionario[string[i]] = i
        i = i + 1
    return dicionario
       
        