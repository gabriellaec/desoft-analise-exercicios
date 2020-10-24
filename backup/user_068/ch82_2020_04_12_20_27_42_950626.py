def primeiras_ocorrencias(a):
    dicionario = {}
    for letra in a:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1
    return dicionario