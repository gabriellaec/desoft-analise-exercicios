def primeiras_ocorrencias (string):
    saida={}
    for l in string:
        if string[l] not in saida:
            saida[string[l]]=l
    return saida