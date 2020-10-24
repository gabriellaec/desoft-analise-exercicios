def primeiras_ocorrencias(palavra):
    string = str(palavra)
    dicionario = {}
    for i in string:
        if not i in dicionario:
            dicionario[i] = i
    return dicionario