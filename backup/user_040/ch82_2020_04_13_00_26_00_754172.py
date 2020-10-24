def primeiras_ocorrencias(x):
    dicionario = {}
    n = 0
    for letra in x:
        if letra not in dicionario.keys():
            dicionario[letra] = x[n]
            n += 1
        else:
            n += 1
    return dicionario