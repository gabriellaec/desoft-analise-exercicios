def conta_ocorrencias (palavras):
    dicionario = {}
    i = 0
    if i in palavras:
        if not i in dicionario:
            dicionario[i] = 1
        else: 
            dicionario[i] = dicionario[i] + 1
    return dicionario