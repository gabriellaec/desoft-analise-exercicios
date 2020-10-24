def conta_letras (palavra):
    i = 0
    dicionario = {}
    while i < len(palavra):
        if palavra[i] in dicionario:
            values = palavra.count(palavra[i])
            dicionario[palavra[i]] = values
        else:
            dicionario[palavra[i]] = 1
        i = i + 1
    return dicionario