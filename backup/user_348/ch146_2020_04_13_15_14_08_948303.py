def conta_ocorrencias (palavras):
    dicionario = {}
    for i in palavras:
        if palavras not in dicionario:
            dicionario[i] = 1
        else: 
            dicionario[i] = dicionario[i] + 1
    return dicionario