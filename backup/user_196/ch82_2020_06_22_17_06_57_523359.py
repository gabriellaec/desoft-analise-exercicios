def primeiras_ocorrencias(a):
    dicionario = {}
    for i in a:
        dicionario[a[i]] = i
    return dicionario