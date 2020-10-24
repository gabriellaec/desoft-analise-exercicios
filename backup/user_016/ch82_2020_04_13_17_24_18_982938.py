def primeiras_ocorrencias(palavra):
    dicionario = {}
    indice = 0
    for i in palavra:
        if i not in dicionario.keys():
            dicionario[i] = indice
        if i in dicionario.keys():
            pass
        indice += 1
    return dicionario