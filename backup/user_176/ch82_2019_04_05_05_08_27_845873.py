def primeiras_ocorrencias(string):
    ocorrencias={}
    for e in range(len(string)-1):
        if string[e] not in ocorrencias:
            ocorrencias[string[e]]=e
    return ocorrencias