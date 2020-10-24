def primeiras_ocorrencias(palavra):
    dicionario = {}
    for letra in palavra:
        if not letra in dicionario:
            dicionario[letra] = palavra[letra]
    return dicionario
            