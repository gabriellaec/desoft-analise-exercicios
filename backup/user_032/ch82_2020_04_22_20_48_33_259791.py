def primeiras_ocorrencias(palavra):
    dicionario = {}
    for i in palavra:
        if i not in dicionario:
            dicionario[i] = palavra.index(i)
    return dicionario