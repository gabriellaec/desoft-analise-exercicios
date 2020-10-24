def conta_letras(string):
    dicionario = {}
    for letra in string:
        if not letra in dicionario:
            dicionario[letra] = 1
        else:
            dicionario[letra] += 1
    return dicionario
        