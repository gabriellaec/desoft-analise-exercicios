def conta_letras (string):
    dicionario = {}
    for letras in string:
        if not letras in dicionario:
            dicionario[letras] = 1
        else:
            dicionario[letras] += 1
    return dicionario