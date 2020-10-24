def primeiras_ocorrencias (string):
    saida={}
    for l in range (0, len(string)-1):
        if string[l] not in saida:
            saida[string[l]]=l
    return saida