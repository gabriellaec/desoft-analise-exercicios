def primeiras_ocorrencias (palavra):
    dicionario = {}
    i = 0
    while i < len(palavra):
        if palavra[i] in dicionario:
            i = i + 1
        else: 
            dicionario[palavra[i]] = i
            i = i + 1
    return dicionario