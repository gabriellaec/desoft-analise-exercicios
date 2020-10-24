def primeiras_ocorrencias(palavra):
    dicionario = {}
    i = 0
    for letra in palavra:
        if not letra in dicionario:
            dicionario[letra] = i
        i+=1
    return dicionario
            