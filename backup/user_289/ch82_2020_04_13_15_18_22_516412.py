def primeiras_ocorrencias(palavra):
    string = str(palavra)
    dicionario = {}
    e = 0
    for i in string:
        if not i in dicionario:
            dicionario[i] = e
            e += 1
        else:
            e += 1
    return dicionario