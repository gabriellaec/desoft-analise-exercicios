def primeiras_ocorrencias(palavra):
    dicionario = {}
    for i in range(len(palavra)):
        if not palavra[i] in dicionario:
            dicionario[palavra[i]] = i
    return dicionario