def primeiras_ocorrencias(palavra):
    dicionario = {}
    indice = 0
    for i in palavra:
        if i not in dicionario.keys():
            dicionario[i] = indice
            indice += 1
        if i in dicionario.keys():
            pass
    return dicionario