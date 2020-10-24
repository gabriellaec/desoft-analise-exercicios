def conta_ocorrencias (palavras):
    dicionario = {}
    for i in palavras:
        if not i in dicionario:
            dicionario[i] = 1
        else: 
            dicionario[i] = dicionario[i] + 1
    return dicionario