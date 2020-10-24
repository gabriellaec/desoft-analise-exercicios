
def primeiras_ocorrencias(a):
    dicionario = {}
    for letra in a:
        if letra not in dicionario:
            dicionario[letra] = a.index(letra)
    return dicionario