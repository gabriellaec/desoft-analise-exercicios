def primeiras_ocorrencias(n):
    dicionario = {}
    for i in range(0, len(n)):
        if n[i] not in dicionario:
            dicionario[n[i]] = i
    return dicionario