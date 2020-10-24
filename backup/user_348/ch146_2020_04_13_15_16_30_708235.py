def conta_ocorrencias (palavras):
    dicionario = {}
    i = 0
    while i < len(palavras):
        if i not in dicionario:
            dicionario[i] = 1
        else: 
            dicionario[i] = dicionario[i] + 1
        i = i + 1
    return dicionario