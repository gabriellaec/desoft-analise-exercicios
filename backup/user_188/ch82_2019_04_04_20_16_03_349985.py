def primeiras_ocorrencias(frase):
    dicionario = {}
    for letra in frase:
        dicionario[letra] = frase.index(letra)
    return dicionario