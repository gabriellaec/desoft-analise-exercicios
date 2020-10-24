def primeiras_ocorrencias(a):
    dicionario = {}
    for i in a:
        if i not in dicionario:
            dicionario[i] = a[i]
    return dicionario